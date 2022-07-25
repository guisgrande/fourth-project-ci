from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventsView.as_view(), name='events'),
    path('add-event/', views.AddEventPost.as_view(), name='add_event'),
    path('edit-event/<slug:slug>/', views.EditEventPost.as_view(), name='edit_event'),
    path('delete-event/<slug:slug>/', views.DeleteEventPost.as_view(), name='delete_event'),
    path('event-detail/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('presence-go-event/<slug:slug>/', views.PresenceGoEvent.as_view(), name='presence_go_event'),
    path('presence-maybe-event/<slug:slug>/', views.PresenceMaybeEvent.as_view(), name='presence_maybe_event'),
]
