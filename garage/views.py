from django.shortcuts import render
from django.views import generic, View
from .models import Car
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from events.models import Event
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
            'more_context': Car.objects.all(),
        })
        return context

    def get_queryset(self):
        return Car.objects.order_by('-created_on')


class GarageView(generic.TemplateView):
    template_name = 'garage.html'


class AddCarPost(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """
    Logged in user can create a car post
    """
    model = Car
    fields = [
        'brand',
        'model',
        'year',
        'price',
        'hp',
        'speed',
        'description',
        'featured_image',
        ]
    template_name = 'members/add_car.html'
    success_url = reverse_lazy('members')
    success_message = "You have added car to the garage!"

    def form_valid(self, form):
        """
        Sets logged in user as username field in form
        Sets form default status to published
        """
        form.instance.username = self.request.user
        form.instance.status = 1
        return super(AddCarPost, self).form_valid(form)

#    def auto_slug(self, form):
#        """
#        Sets slug field to auto field
#        """
#
#        first_field = self.request.user
#        second_field = self.request.model
#        third_field = self.request.year
#        autofield = first_field + second_field + third_field
#        
#        form.instance.slug = autofield
#        return super(AddCarPost, self).form_valid(form)