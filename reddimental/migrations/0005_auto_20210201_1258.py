# Generated by Django 2.2.10 on 2021-02-01 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reddimental', '0004_auto_20210201_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 9, 58, 23, 282620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 9, 58, 23, 281625, tzinfo=utc)),
        ),
    ]
