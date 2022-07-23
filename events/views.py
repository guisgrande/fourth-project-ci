from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
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


class AddEventPost(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """
    Logged in user can create a event post.
    """
    model = Event
    fields = [
        'event_title',
        'category',
        'start_date',
        'start_time',
        'description',
        'local',
        'event_image',
        ]
    template_name = 'events/add_event.html'
    success_url = reverse_lazy('members')
    success_message = "You event was added to Events!"

    def form_valid(self, form):
        """
        Sets logged in user as username field in form
        Sets form default status to published
        """
        form.instance.username = self.request.user
        form.instance.status = 1
        return super(AddEventPost, self).form_valid(form)


class EditEventPost(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Logged in user can edit your event details.
    From My Event list page.
    """
    model = Event
    fields = [
        'event_title',
        'category',
        'start_date',
        'start_time',
        'description',
        'local',
        'event_image',
        ]
    template_name = 'events/add_event.html'
    success_url = reverse_lazy('members')
    success_message = "All right! You updated your event details. Thanks."
