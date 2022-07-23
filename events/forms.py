from .models import CommentEvent
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentEvent
        fields = ('body',)