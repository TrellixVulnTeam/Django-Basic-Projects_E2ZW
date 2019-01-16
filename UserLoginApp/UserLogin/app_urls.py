from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/logged-in/login/', views.loging, name='login'),
    path('user/logged-in/dashboard/', views.dashboard),
    path('logout/', views.logout)
]