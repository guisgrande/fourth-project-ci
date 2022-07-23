from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventsView.as_view(), name='events'),
    path('addevent/', views.AddEventPost.as_view(), name='add_event'),
    path('editevent/<slug:slug>/', views.EditEventPost.as_view(), name='edit_event'),
    path('eventdetail/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
