from django.contrib import admin
from django.urls import re_path
from DjangoApp.views import HomeView, view_details



urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name="home"),
    re_path(r'about/me/<slug:slug>^$',view_details),
]
