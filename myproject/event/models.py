from django.db import models
from club.models import Club

# Create your models here.
class Event(models.Model):
    EventId             = models.AutoField(primary_key=True)
    EventName           = models.CharField(max_length = 150)
    EventImageName      = models.TextField(null=True, blank=True)
    EventImage          = models.ImageField(upload_to='images', null=True, blank=True)
    ClubName            = models.ForeignKey(Club, on_delete=models.CASCADE)
    EventType           = models.CharField(max_length = 150)
    EventEligibility    = models.CharField(max_length = 150)
    EventStatus         = models.CharField(max_length = 10, default=False)
    EventApproval       = models.CharField(max_length = 10, default= -1)
    EventStartDate      = models.CharField(max_length = 150)
    EventEndDate        = models.CharField(max_length = 150)
    EventDescription    = models.TextField()
    EventAmount         = models.IntegerField()
    
    