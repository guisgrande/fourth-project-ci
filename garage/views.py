from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Car, RateCar
from .forms import CommentForm, RateForm


class GarageView(generic.ListView):
    """
    Class to display all cars posts at garage page.
    Ordered by new one show first an paginated by 6.
    """
    model = Car
    template_name = 'garage/garage.html'
    context_object_name = 'car_list'
    queryset = Car.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6


class CarDetail(View):
    """
    Class to display car details.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Car.objects.filter(status=1)
        car = get_object_or_404(queryset, slug=slug)
        car_comments = car.car_comments.filter(approved=True).order_by("-created_on")
        car_rate = car.car_rate.filter(rated=True).order_by("-created_on")

        favourited = False
        rated = False

        len_rate = len(car_rate)
        if len_rate == 0:
            len_rate = "0"

        if car_rate.filter(name=self.request.user).exists():
            rated = True

        if car.favourite.filter(id=self.request.user.id).exists():
            favourited = True

        return render(request, "garage/car_details.html", {
            "car": car,
            "car_comments": car_comments,
            "commented": False,
            "car_rate": car_rate,
            "len_rate": len_rate,
            "rated": rated,
            "favourited": favourited,
            "comment_form": CommentForm(),
            })
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Car.objects.filter(status=1)
        car = get_object_or_404(queryset, slug=slug)
        car_comments = car.car_comments.filter(approved=True).order_by("-created_on")
        comment_form = CommentForm(data=request.POST)
        favourited = False

        #Favourite
        if car.favourite.filter(id=self.request.user.id).exists():
            favourited = True

        # Comment
        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(request, "garage/car_details.html", {
            "car": car,
            "car_comments": car_comments,
            "commented": True,
            "favourited": favourited,
            "comment_form": CommentForm()
            })


class RateCarView(LoginRequiredMixin, View):
    """
    Class view to display Rate car reviews.
    To display form and data from user.
    """
    model = RateCar
    template_name = 'garage/rate_car.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = Car.objects.filter(status=1)
        car = get_object_or_404(queryset, slug=slug)
        car_rate = car.car_rate.filter(rated=True).order_by("-created_on")
        rated = False
        rate_form = RateForm()

        if car_rate.filter(name=self.request.user).exists():
            rated = True
        
        return render(request, "garage/rate_car.html", {
            "car": car,
            "car_rate": car_rate,
            "rated": rated,
            "rate_form": RateForm()
            })
        
    def post(self, request, slug, *args, **kwargs):
        queryset = Car.objects.filter(status=1)
        car = get_object_or_404(queryset, slug=slug)
        car_rate = car.car_rate.all()
        rate_form = RateForm(data=request.POST)

        # Rate
        if rate_form.is_valid():
            rate = rate_form.save(commit=False)
            rate.name = request.user
            rate.car = car
            rate.rated = True
            rate.save()
        else:
            rate_form = RateForm()

        return render(request, "garage/rate_car.html", {
            "car": car,
            "car_rate": car_rate,
            "rated": True,
            "rate_form": RateForm()
            })


class FavouriteCar(LoginRequiredMixin, View):
    """
    Class to logged user favourite or unfavorite car post.
    """ 
    def post(self, request, slug, *args, **kwargs):
        car = get_object_or_404(Car, slug=slug)
        if car.favourite.filter(id=request.user.id).exists():
            car.favourite.remove(request.user)
        else:
            car.favourite.add(request.user)

        return HttpResponseRedirect(reverse('car_detail', args=[slug]))


class AddCarPost(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """
    Logged in user can create a car post.
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
    template_name = 'garage/add_car.html'
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


class EditCarPost(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Logged in user can edit your car details.
    From My Cars list page.
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
    template_name = 'garage/add_car.html'
    success_url = reverse_lazy('members')
    success_message = "All right! You updated your car details. Thanks."


class DeleteCarPost(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """
    Logged in user can delete your car.
    From My Cars list page.
    """
    model = Car
    success_url = reverse_lazy('members')
    success_message = "It's done! You deleted your car post."
    template_name = 'garage/delete_car.html'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteCarPost, self).delete(request, *args, **kwargs)