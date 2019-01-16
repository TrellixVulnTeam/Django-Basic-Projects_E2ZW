from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/<int:id>/action/edit/', views.EditPage),
    path('user/<int:id>/action/delete/', views.delete),
]