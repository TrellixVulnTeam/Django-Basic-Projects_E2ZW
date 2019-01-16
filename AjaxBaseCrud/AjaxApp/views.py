from django.shortcuts import render, redirect
from django.views import View
from  AjaxApp.models import Student


class Ajax_Base_Crud(View):

    template_name = "ajax_base_crud.html"

    def get(self, request):
        return render(request, self.template_name)
