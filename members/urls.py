from . import views
from django.urls import path
from members.views import deleteuser

urlpatterns = [
    path('members/', views.MemberArea.as_view(), name='members'),
    path('delete/', deleteuser, name='delete'),
]