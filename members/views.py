from django.shortcuts import render
from django.views import generic, View

class MemberArea(generic.TemplateView):
    template_name = 'members/user_area.html'
