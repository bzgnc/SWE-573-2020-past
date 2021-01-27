import uuid
from datetime import datetime

from django.db import models


# Create your models here.

class Submission(models.Model):
    submission_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=datetime.now())
    author = models.TextField(default='')
    title = models.TextField(default='')


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=datetime.now())
    author = models.TextField(default='')
    comment_text = models.TextField(default='')
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
