from . import views
from django.urls import path
from .views import AddCarPost

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('garage/', views.GarageView.as_view(), name='garage'),
    path('addcar/', views.AddCarPost.as_view(), name='add_car'),
]