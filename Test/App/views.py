from django.shortcuts import render, redirect
from App.forms import StudentForm
from django.contrib import messages
from App.models import StudentModel


def index(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           StudentModel.objects.create(name=name, email = email)
           messages.success(request,  "Successfully inserted")
           return render(request, 'index.php', {'form':form})
        else:
           print(form.errors)
    else:
        form = StudentForm()
    
    return render(request, 'index.php', {'form': form})