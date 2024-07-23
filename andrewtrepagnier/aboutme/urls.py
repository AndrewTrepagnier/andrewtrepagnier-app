# pages/urls.py
from django.urls import path
from .views import Viewofaboutme

urlpatterns = [
    path("", Viewofaboutme.as_view(), name="aboutme"),
]