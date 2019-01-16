from django.urls import path
from DjangoApp.views import index
from  django.contrib.auth import login, logout




urlpatterns = [
    path('', index),
    path('login/', login),
]