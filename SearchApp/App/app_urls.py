from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student),
    path('student_list/', views.student_list),
    path('search/', views.search),
]