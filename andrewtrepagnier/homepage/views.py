from django.shortcuts import render
from .models import HomePage
from django.views.generic import TemplateView

class ViewofCover(TemplateView):
    template_name = "homepage.html"
