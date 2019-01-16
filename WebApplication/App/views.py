from django.shortcuts import render, redirect
from django.views import View
from App.models import User
from django.utils.datastructures import MultiValueDictKeyError
import re
from django.db import IntegrityError





# Dashboard incoming page
class DashboardHomeView(View):
    template_name = "admin/home_content/home_content.html"
    def get(self, request):
        user = User.objects.all()
        return render(request, self.template_name, {'users':user})




# add new clients
class DashboardAddNewView(View):
    template_name = "admin/add_new_content/add_new_content.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass