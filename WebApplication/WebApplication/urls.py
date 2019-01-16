from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    #admin urls
    path('admin/controller/dashboard', views.DashboardHomeView.as_view(), name="dashboard_home"),
    path('admin/controller/dashboard/add', views.DashboardAddNewView.as_view(), name="add_new_user"),
]
