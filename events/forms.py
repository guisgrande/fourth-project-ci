from .models import Event, CommentEvent
from cloudinary.forms import CloudinaryFileField
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.DateInput):
    input_type = 'time'


class EventForm(forms.ModelForm):

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
    class Meta:
        model = CommentEvent
        fields = ('body',)