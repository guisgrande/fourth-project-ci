from django.shortcuts import render
from django.views import generic, View
from .models import Car


class CarList(generic.ListView):
    model = Car
    queryset = Car.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class GarageView(generic.TemplateView):
    template_name = 'garage.html'