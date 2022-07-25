from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Event
from .forms import CommentForm


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
        event_comments = event.event_comments.filter(approved=True).order_by("-created_on")

        # Presence confirm
        presence_go_ok = False
        presence_maybe_ok = False

        if event.presence_go.filter(id=self.request.user.id).exists():
            presence_go_ok = True

        if event.presence_maybe.filter(id=self.request.user.id).exists():
            presence_maybe_ok = True

        return render(request, "events/event_details.html", {
            "event": event,
            "presence_go_ok": presence_go_ok,
            "presence_maybe_ok": presence_maybe_ok,
            "event_comments": event_comments,
            "commented": False,
            "comment_form": CommentForm()
            })

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        event_comments = event.event_comments.filter(approved=True).order_by("-created_on")
        comment_form = CommentForm(data=request.POST)

        # Comment form confirmation
        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
        else:
            comment_form = CommentForm()

        # Presence confirm
        presence_go_ok = False
        presence_maybe_ok = False

        if event.presence_go.filter(id=self.request.user.id).exists():
            presence_go_ok = True

        if event.presence_maybe.filter(id=self.request.user.id).exists():
            presence_maybe_ok = True
        
        return render(request, "events/event_details.html", {
            "event": event,
            "presence_go_ok": presence_go_ok,
            "presence_maybe_ok": presence_maybe_ok,
            "event_comments": event_comments,
            "commented": True,
            "comment_form": CommentForm()
            })


class PresenceGoEvent(LoginRequiredMixin, View):
    """
    Class to logged user tag go an event.
    """ 
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        go_filter = event.presence_go.filter(id=request.user.id)
        maybe_filter = event.presence_maybe.filter(id=request.user.id)

        if go_filter.exists():
            event.presence_go.remove(request.user)
        else:
            event.presence_go.add(request.user)
            if maybe_filter.exists():
                event.presence_maybe.remove(request.user)
            else:
                pass

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class PresenceMaybeEvent(LoginRequiredMixin, View):
    """
    Class to logged user tag maybe go an event.
    """ 
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        go_filter = event.presence_go.filter(id=request.user.id)
        maybe_filter = event.presence_maybe.filter(id=request.user.id)

        if maybe_filter.exists():
            event.presence_maybe.remove(request.user)
        else:
            event.presence_maybe.add(request.user)
            if go_filter.exists():
                event.presence_go.remove(request.user)
            else:
                pass

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


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


class DeleteEventPost(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """
    Logged in user can delete your event.
    From My Events list page.
    """
    model = Event
    success_url = reverse_lazy('members')
    success_message = "It's done! You deleted your event post."
    template_name = 'events/delete_event.html'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteEventPost, self).delete(request, *args, **kwargs)
