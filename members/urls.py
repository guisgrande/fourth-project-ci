from . import views
from django.urls import path
from members.views import deleteuser, membercars, memberevents

urlpatterns = [
    path('members/', views.MemberArea.as_view(), name='members'),
    path('membercars/', membercars, name='membercars'),
    path('memberevents/', memberevents, name='memberevents'),
    path('delete/', deleteuser, name='delete'),
]
