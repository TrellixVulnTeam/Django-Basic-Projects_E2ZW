from django.urls import path
from App import views

urlpatterns = [
    path('',views.home, name="home"),
    path('details/<slug:slug>/<int:id>',views.details, name="details"),
]