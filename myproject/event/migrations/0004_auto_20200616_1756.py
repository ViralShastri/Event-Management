# Generated by Django 3.0.5 on 2020-06-16 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20200616_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 6, 16, 12, 25, 58, 491739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 6, 16, 12, 25, 58, 491739, tzinfo=utc)),
        ),
    ]
