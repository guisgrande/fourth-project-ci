from django.shortcuts import render
from django.views import generic, View
from events.models import Event
from garage.models import Car

class IndexView(generic.ListView):
    """
    Class used to display index content list.
    Show last cars and events at index page.
    """
    template_name = 'index.html'
    context_object_name = 'car_list'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'event_list': Event.objects.order_by('-created_on'),
        })
        return context

    def get_queryset(self):
        return Car.objects.order_by('-created_on')[:4]
