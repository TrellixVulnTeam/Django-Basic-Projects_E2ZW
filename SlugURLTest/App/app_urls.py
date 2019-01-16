from django.urls import path
from App import views


urlpatterns = [
    path("", views.home, name="home"),
    path("details/<slug:slug>", views.view, name="view")
]