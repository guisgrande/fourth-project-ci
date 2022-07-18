from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class MemberArea(generic.TemplateView):
    """
    Class used to display member areas page.
    """
    template_name = 'members/user_area.html'


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