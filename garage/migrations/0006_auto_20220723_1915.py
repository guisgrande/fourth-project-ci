# Generated by Django 3.2.14 on 2022-07-23 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garage', '0005_commentcar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='favorite',
        ),
        migrations.AddField(
            model_name='car',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite_car', to=settings.AUTH_USER_MODEL),
        ),
    ]
