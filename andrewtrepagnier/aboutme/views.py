from django.shortcuts import render
from .models import Aboutme
from django.views.generic import TemplateView

class Viewofaboutme(TemplateView):
    template_name = "aboutme.html"
