from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/<int:id>", views.index, name="about"),
]