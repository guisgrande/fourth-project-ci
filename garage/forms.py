from .models import Car, CommentCar, RateCar
from django import forms


class CarForm(forms.ModelForm):
    """
    Form class to create car post.
    """
    brand = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Ex: Ford, Porsche, ...'}
        ))
    model = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Ex: Mustang, 911, ...'}
        ))
    year = forms.IntegerField(widget=forms.NumberInput(
        attrs={'min': '1807', 'max': '2022', 'step': '1'}
        ))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'min': '0'}))
    hp = forms.FloatField(widget=forms.NumberInput(attrs={'min': '0'}))
    speed = forms.FloatField(widget=forms.NumberInput(attrs={'min': '0'}))

    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'year',
            'price',
            'hp',
            'speed',
            'description',
            'car_image',
        ]


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
