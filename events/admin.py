from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventsAdmin(SummernoteModelAdmin):

    list_display = ('username', 'slug', 'category', 'status', 'created_on')
    search_fields = ['username', 'event_title', 'category']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('username', 'event_title',)}
    summernote_fields = ('description')
