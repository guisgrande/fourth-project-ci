from django.shortcuts import render
from django.views import generic, View
from .models import Event


#class EventList(generic.ListView):
#    model = Event
#    queryset = Event.objects.filter(status=1).order_by('-created_on')
#    template_name = 'events.index.html'
#    paginate_by = 4


class EventsView(generic.TemplateView):
    template_name = 'events/events.html'