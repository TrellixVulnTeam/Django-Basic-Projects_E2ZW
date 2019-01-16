from django.urls import path
from FirstProject import views

urlpatterns = [
    path("", views.home, name = "home"),
]