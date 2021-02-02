from datetime import datetime

from django.shortcuts import render
from .forms import SubredditForm
from .models import Submission, Comment
from .praw_reddit_scraper import RedditScrapeManager
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


# Create your views here.
def index(request):
    subreddit_form = SubredditForm()
    return render(request, 'index.html', {'subreddit_form': subreddit_form})


def about(request):
    return render(request, 'about.html')


@login_required(login_url="/accounts/login/")
def analyze_sentiment(request):
    subreddit = request.GET.get('subreddit')
    # Initialize instance of RedditScrapeManager, to call methods on
    scrape_instance = RedditScrapeManager(subreddit)
    # Get subreddit title, subscriber count, and description for banner
    subreddit_info = scrape_instance.get_subreddit_info()
    # Get all submission/comment info
    master_submission_data_list = scrape_instance.get_submission_data()
    # Calculate total average sentiment score from all submissions, and append to subreddit_info dictionary
    subreddit_total_sentiment_score = 0
    subreddit_total_num_comments = 0
    for submission in master_submission_data_list:
        subreddit_total_num_comments += len(submission['comments'])
        subreddit_total_sentiment_score += submission['average_sentiment_score'] * (len(submission['comments']))

    subreddit_average_sentiment_score = subreddit_total_sentiment_score / subreddit_total_num_comments
    subreddit_info['average_sentiment_score'] = round(subreddit_average_sentiment_score, 1)

    sia = SIA()
    qs1 = Submission.objects.filter(title__icontains=subreddit).distinct()
    x = [x.title for x in qs1]
    y = [sia.polarity_scores(y.title)['compound'] * 100 for y in qs1]
    chart1 = RedditScrapeManager.get_plot1(x, y)

    qs2 = Comment.objects.all().distinct()
    x = [x.comment_text for x in qs2]
    y = [sia.polarity_scores(y.comment_text)['compound'] * 100 for y in qs2]
    chart2 = RedditScrapeManager.get_plot2(x, y)

    qs3 = Comment.objects.all().distinct()
    results = []
    results = [sia.polarity_scores(x.comment_text) for x in qs3]
    df = pd.DataFrame.from_records(results)
    df['label'] = 0
    df.loc[df['compound'] > 0.1, 'label'] = 1
    df.loc[df['compound'] < -0.1, 'label'] = -1
    counts = df.label.value_counts(normalize=True) * 100
    x = counts.index
    y = counts
    chart3 = RedditScrapeManager.get_plot3(x, y)

    qs4 = Submission.objects.filter(title__icontains=subreddit).distinct()
    results = []
    for x in qs4:
        scores = sia.polarity_scores(x.title)
        scores['timestamp'] = x.timestamp
        results.append(scores)
    df = pd.DataFrame.from_records(results)
    df.loc[df['compound'] > 0.1, 'label'] = 1
    df.loc[df['compound'] < -0.1, 'label'] = -1
    x1 = df[df['label'] == -1].timestamp
    x2 = df[df['label'] == 1].timestamp
    y1 = df[df['label'] == -1].compound
    y2 = df[df['label'] == 1].compound
    chart4 = RedditScrapeManager.get_plot4(x1, y1, x2, y2)

    if scrape_instance.sub_exists():
        args = {'subreddit': subreddit, 'subreddit_info': subreddit_info,
                'master_submission_data_list': master_submission_data_list, 'chart1': chart1, 'chart2': chart2,
                'chart3': chart3, 'chart4': chart4}
        return render(request, 'analyze_sentiment.html', args)

    '''
    Form validation logic. WIP.
    else:
        form = SubredditForm()
        return render(request, 'index.html', {'subreddit_form': form})
    '''
