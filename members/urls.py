from . import views
from django.urls import path
from members.views import deleteuser, membercars

urlpatterns = [
    path('members/', views.MemberArea.as_view(), name='members'),
    path('membercars/', membercars, name='membercars'),
    path('delete/', deleteuser, name='delete'),
]