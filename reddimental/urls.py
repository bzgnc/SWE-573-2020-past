from django.urls import path
from reddimental import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('analyze_sentiment/', views.analyze_sentiment, name="analyze_sentiment")
]