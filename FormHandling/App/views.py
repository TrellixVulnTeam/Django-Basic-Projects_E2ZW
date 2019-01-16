from django.shortcuts import render, redirect
from django.contrib import messages
from App.forms import ValidationForm
from App.models import StudentModel



def index(request):
    if request.method =="POST":
        form = ValidationForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            StudentModel.objects.create(title=title)
            messages.success(request, "Saved successfully!")
            return redirect('home')
        else:
            form = ValidationForm()
            return render(request,'form.html', {'form':form})
    else:
        form = ValidationForm()
        return render(request,'form.html',{'form':form})