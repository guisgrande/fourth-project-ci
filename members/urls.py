from . import views
from django.urls import path

urlpatterns = [
    path('members/', views.MemberArea.as_view(), name='members'),
]