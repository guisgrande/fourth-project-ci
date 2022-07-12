from django.contrib import admin
from .models import Car
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Car)
class GarageAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
