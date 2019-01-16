from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
]
