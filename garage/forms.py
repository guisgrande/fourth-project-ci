from .models import CommentCar, RateCar
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class to comment car post.
    """
    class Meta:
        model = CommentCar
        fields = ('body',)


class RateForm(forms.ModelForm):
    """
    Form class to rate car post.
    """
    class Meta:
        model = RateCar
        fields = ('price', 'aesthetics', 'speed', 'drivability', 'overall',)
        labels = {
            'price': ('Price: '),
            'aesthetics': ('Aesthetics: '),
            'speed': ('Speed: '),
            'drivability': ('Drivability: '),
            'overall': ('Overall: ')
        }
