from django.shortcuts import render
from django.views import generic, View
from .models import Car
from events.models import Event

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'car_list'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'event_list': Event.objects.order_by('-created_on'),
            'more_context': Car.objects.all(),
        })
        return context

    def get_queryset(self):
        return Car.objects.order_by('-created_on')


class GarageView(generic.TemplateView):
    template_name = 'garage.html'