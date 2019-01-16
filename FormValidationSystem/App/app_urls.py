from django.urls import path
from App import views


urlpatterns = [
    path("", views.FormView.as_view(), name="form"),
]