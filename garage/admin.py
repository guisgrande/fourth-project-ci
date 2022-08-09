from django.contrib import admin
from .models import Car, CommentCar, RateCar
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Car)
class GarageAdmin(SummernoteModelAdmin):

    list_display = (
        'username',
        'slug',
        'brand',
        'model',
        'status',
        'created_on')
    search_fields = ['username', 'brand', 'model']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('username', 'model', 'year',)}
    summernote_fields = ('description')


@admin.register(CommentCar)
class CommentCarAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'car', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'car', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(RateCar)
class RateCarAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'created_on',
        'price',
        'aesthetics',
        'speed',
        'drivability',
        'overall'
        )
