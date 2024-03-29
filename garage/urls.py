from . import views
from django.urls import path


urlpatterns = [
    path('garage/', views.garage, name='garage'),
    path('add-car/', views.AddCarPost.as_view(), name='add_car'),
    path(
        'edit-car/<slug:slug>/',
        views.EditCarPost.as_view(),
        name='edit_car'
        ),
    path(
        'delete-car/<slug:slug>/',
        views.DeleteCarPost.as_view(),
        name='delete_car'
        ),
    path(
        'car-detail/<slug:slug>/',
        views.CarDetail.as_view(),
        name='car_detail'
        ),
    path(
        'favourite/<slug:slug>/',
        views.FavouriteCar.as_view(),
        name='favourite_car'
        ),
    path(
        'rate-car/<slug:slug>/',
        views.RateCarView.as_view(),
        name='rate_car'
        ),
    path('search-car/', views.search_car, name='search_car'),
    path('load-more-cars/', views.load_more_cars, name='load_more_cars'),
]
