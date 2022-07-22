from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventsView.as_view(), name='events'),
    path('eventdetail/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]