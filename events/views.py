from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Event


class EventsView(generic.ListView):
    """
    Class to display all event posts at events page.
    Ordered by new one show first an paginated by 6.
    """
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'event_list'
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6

class EventDetail(View):
    """
    Class to display event details.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
    
        return render(request, "events/event_details.html", {"event": event})

