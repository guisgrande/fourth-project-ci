from . import views
from django.urls import path


urlpatterns = [
    path('garage/', views.GarageView.as_view(), name='garage'),
    path('add-car/', views.AddCarPost.as_view(), name='add_car'),
    path('edit-car/<slug:slug>/', views.EditCarPost.as_view(), name='edit_car'),
    path('delete-car/<slug:slug>/', views.DeleteCarPost.as_view(), name='delete_car'),
    path('car-detail/<slug:slug>/', views.CarDetail.as_view(), name='car_detail'),
]