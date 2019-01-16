from django.shortcuts import render, redirect
from django.views import View
from .models import Student_Info


def index(request):
	if request.method == 'POST':
        pass
