from django.contrib import admin
from .models import Event, CommentEvent
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventsAdmin(SummernoteModelAdmin):

    list_display = ('username', 'slug', 'category', 'status', 'created_on')
    search_fields = ['username', 'event_title', 'category']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('username', 'event_title',)}
    summernote_fields = ('description')


@admin.register(CommentEvent)
class CommentEventAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'body', 'event', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'event', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)