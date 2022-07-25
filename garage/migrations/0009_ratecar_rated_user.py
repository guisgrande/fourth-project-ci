# Generated by Django 3.2.14 on 2022-07-25 13:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garage', '0008_ratecar_rated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratecar',
            name='rated_user',
            field=models.ManyToManyField(blank=True, related_name='rated_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
