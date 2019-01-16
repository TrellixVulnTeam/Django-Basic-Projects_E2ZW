from django.urls import path
from App.views import home

urlpatterns = [
	path('', home),
]