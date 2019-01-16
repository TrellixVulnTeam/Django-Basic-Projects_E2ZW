from django.shortcuts import render
from django.views import View
from App.models import Employee
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError


class FormView(View):

    template_name = 'form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            user_qualification = request.POST['user_qualification']
            if user_qualification.__ne__(None):
                emp = Employee()
                emp.user_qualification = user_qualification
                emp.save()
                return render(request, self.template_name, {"message": "inserted"})

        except MultiValueDictKeyError:
            return render(request, self.template_name, {"message": "Must be selected one"})

