from django.shortcuts import render
from .models import Tackboard
from django.views.generic import TemplateView

class ViewofTackboard(TemplateView):
    template_name = 'tackboard.html'
