from . import views
from django.urls import path

urlpatterns = [
    path('', views.CarList.as_view(), name='home')
]