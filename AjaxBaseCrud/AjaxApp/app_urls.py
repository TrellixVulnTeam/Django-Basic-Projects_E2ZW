from django.urls import path
from AjaxApp import views


urlpatterns = [
    path('', views.Ajax_Base_Crud.as_view()),
]