from django.db import models
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
    event_date = models.DurationField()
    local = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
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

    class Meta:
        """
        Class to show newest event first 
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.event_id