from django.urls import path
from . import views




urlpatterns = [
    path('', views.index),
    path('upload/', views.upload),
    path('edit_page/<int:id>', views.edit_page),
    path('update/<int:id>', views.update),
]