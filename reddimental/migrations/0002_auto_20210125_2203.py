# Generated by Django 2.2.10 on 2021-01-25 19:03

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reddimental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 22, 3, 19, 466223)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 22, 3, 19, 465225)),
        ),
    ]
