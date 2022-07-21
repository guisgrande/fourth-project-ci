from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Car


class GarageView(generic.ListView):
    model = Car
    template_name = 'garage.html'
    context_object_name = 'car_list'
    queryset = Car.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6


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
        'car_image',
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
