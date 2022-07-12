from django.contrib import admin
from .models import Car
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Car)
class GarageAdmin(SummernoteModelAdmin):

    list_display = ('username', 'slug', 'brand', 'model', 'status', 'created_on')
    search_fields = ['username', 'brand', 'model']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('username', 'model', 'year',)}
    summernote_fields = ('description')
