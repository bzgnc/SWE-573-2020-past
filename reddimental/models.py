import uuid
from datetime import datetime

from django.db import models
from django.utils import timezone
import pytz


# Create your models here.

class Submission(models.Model):
    submission_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.TextField(default='', null=True)
    title = models.TextField(default='', null=True)


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.TextField(default='', null=True)
    comment_text = models.TextField(default='', null=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
