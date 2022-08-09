from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from garage.models import Car
from events.models import Event


class MemberArea(generic.TemplateView):
    """
    Class used to display member areas page.
    """
    template_name = 'members/user_area.html'


@login_required
def membercars(request):
    """
    Function filter just the car of the current user
    and display at user 'My cars' page.
    """
    current_user = request.user.id
    context = {}
    context['user_car_list'] = Car.objects.filter(
        username_id=current_user
        ).order_by('-created_on')
    return render(request, "members/user_cars.html", context)


@login_required
def memberevents(request):
    """
    Function filter just the events of the current user
    and display at user 'My events' page.
    """
    current_user = request.user.id
    context = {}
    context['user_event_list'] = Event.objects.filter(
        username_id=current_user
        ).order_by('-created_on')
    return render(request, "members/user_events.html", context)


@login_required
def deleteuser(request):
    """
    Function for delete account, permanently.
    """
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('home')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'members/delete_account.html', context)
