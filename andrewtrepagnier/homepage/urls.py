# pages/urls.py
from django.urls import path
from .views import ViewofCover

urlpatterns = [
    path('', ViewofCover.as_view(), name="home"),
]