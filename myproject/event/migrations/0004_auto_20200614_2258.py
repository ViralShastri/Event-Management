# Generated by Django 3.0.5 on 2020-06-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20200614_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='EventEndTime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventStartTime',
        ),
    ]
