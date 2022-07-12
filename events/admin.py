from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventsAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
