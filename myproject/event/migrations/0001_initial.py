# Generated by Django 3.0.5 on 2020-06-16 11:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0009_clubmember'),
        ('venue', '0002_auto_20200519_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('EventId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('EventImageName', models.TextField(blank=True, null=True)),
                ('EventImage', models.ImageField(blank=True, null=True, upload_to='images')),
                ('EventType', models.CharField(max_length=150)),
                ('EventEligibility', models.CharField(max_length=150)),
                ('EventStatus', models.CharField(default=False, max_length=10)),
                ('EventApproval', models.CharField(default=-1, max_length=10)),
                ('start', models.DateField(default=datetime.date.today)),
                ('end', models.DateField(default=datetime.date.today)),
                ('EventStartTime', models.TimeField(default=datetime.datetime(2020, 6, 16, 11, 57, 20, 898377, tzinfo=utc))),
                ('EventEndTime', models.TimeField(default=datetime.datetime(2020, 6, 16, 11, 57, 20, 898377, tzinfo=utc))),
                ('EventDescription', models.TextField()),
                ('EventAmount', models.IntegerField()),
                ('ClubName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Club')),
                ('VenueId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.Venue')),
            ],
        ),
    ]
