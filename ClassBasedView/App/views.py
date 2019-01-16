from django.shortcuts import render
from App.models import Student
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView


class AddEmployee(CreateView):
    model = Student
    template_name = 'add_employee.html'
    fields = "__all__"
    success_url = reversed('/')



