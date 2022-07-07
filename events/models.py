import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Event(models.Model):
    """
    Class to represent Event database model
    """
    event_id = models.SmallAutoField(primary_key=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='event_post'
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    event_title = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    local = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    featured_image = CloudinaryField('image', default='placeholder')
    
    ROAD = 'Road Trip'
    TRACK = 'Track Day'
    EXPO = 'Exposition'
    TRADE = 'Trade Event'
    MEET = 'Meeting Event'
    OTHER = 'Other Events'

    EVENT_CATEGORIES = [
        (ROAD, 'Road Trip'),
	    (TRACK, 'Track Day'),
	    (EXPO, 'Exposition'),
	    (TRADE, 'Trade Event'),
	    (MEET, 'Meeting Event'),
	    (OTHER, 'Other Events')
    ]

    category = models.CharField(
        max_length=15,
        choices=EVENT_CATEGORIES,
        blank=False, default=OTHER
        )
        
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Class to show newest event first 
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.event_id)