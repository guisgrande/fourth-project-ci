from .models import Event, CommentEvent
from cloudinary.forms import CloudinaryFileField
from django import forms


class DateInput(forms.DateInput):
    """
    Form class set up date input.
    """
    input_type = 'date'


class TimeInput(forms.DateInput):
    """
    Form class set up time input.
    """
    input_type = 'time'


class EventForm(forms.ModelForm):
    """
    Form class to create event post.
    """
    event_image = CloudinaryFileField(
        options = { 
            'crop': 'limit', 'width': 1280, 'height': 720,
    })

    class Meta:
        model = Event
        fields = [
            'event_title',
            'category',
            'start_date',
            'start_time',
            'local',
            'description',
            'event_image',
        ]
        widgets = {
            'start_date': DateInput(),
            'start_time': TimeInput(),
        }


class CommentForm(forms.ModelForm):
    """
    Form class to comment event post.
    """
    class Meta:
        model = CommentEvent
        fields = ('body',)