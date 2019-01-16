from django.urls import path
from . import views




urlpatterns=[
    path("", views.SaveData.as_view()),
    path("<int:id>/Edit/", views.UpdateData.as_view()),
    path("login/", views.LoginView.as_view()),
]