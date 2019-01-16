from django.shortcuts import render, redirect
from .models import Employee


def index(request):
    emp = Employee.objects.all()
    return render(request, 'index.html', {'employee':emp})


def upload(request):
    emp = Employee(
        name=request.POST['name'],
        image=request.FILES['image']
    )
    emp.save()
    success = "Data inserted"

    return render(request, 'index.html', {'scs':success})


def edit_page(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'edit_page.html',{'employee':emp})



def update(request, id):

    emp = Employee.objects.get(id=id)
    emp.name = request.POST['name']
    emp.image = request.FILES['image'] or None

    return redirect('/')