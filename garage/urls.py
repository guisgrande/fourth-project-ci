from . import views
from django.urls import path

urlpatterns = [
    path('', views.CarList.as_view(), name='home'),
    path('garage/', views.GarageView.as_view(), name='garage'),
]