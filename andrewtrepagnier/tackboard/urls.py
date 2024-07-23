# pages/urls.py
from django.urls import path
from .views import ViewofTackboard

urlpatterns = [
    path('tackboard/', ViewofTackboard.as_view(), name='tackboard'),
]