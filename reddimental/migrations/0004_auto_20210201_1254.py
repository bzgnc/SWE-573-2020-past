# Generated by Django 2.2.10 on 2021-02-01 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddimental', '0003_auto_20210201_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 12, 54, 9, 188928)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 12, 54, 9, 187932)),
        ),
    ]
