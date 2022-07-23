from .models import CommentCar
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentCar
        fields = ('body',)
