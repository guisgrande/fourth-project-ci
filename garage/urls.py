from . import views
from django.urls import path


urlpatterns = [
    path('garage/', views.GarageView.as_view(), name='garage'),
    path('addcar/', views.AddCarPost.as_view(), name='add_car'),
    path('cardetail/<slug:slug>/', views.CarDetail.as_view(), name='car_detail'),
]