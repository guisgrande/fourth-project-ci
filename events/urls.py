from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventsView.as_view(), name='events'),
]