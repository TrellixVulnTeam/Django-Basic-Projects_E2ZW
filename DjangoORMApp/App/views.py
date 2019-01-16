from django.shortcuts import render, redirect
from .models import Student, Name


def index(request):
    if request.method == 'POST':
        student = Student()
        name = Name()
        name.first_name = request.POST['fname']
        name.last_name = request.POST['lname']
        name.save()
        student.fathers_name = request.POST['ftname']
        student.mothers_name = request.POST['mtname']
        student.name = Name.objects.get(id=name.id)
        student.save()
        return redirect('/')
    else:
        student = Student.objects.all()
        return render(request, 'index.html', {'student':student})


def EditPage(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        name = Name.objects.get(id=id)

        name.first_name = request.POST['fname']
        name.last_name = request.POST['lname']
        name.save()

        student.fathers_name = request.POST['ftname']
        student.mothers_name = request.POST['mtname']
        student.name = Name.objects.get(id=name.id)
        student.save()

        return redirect('/')
    else:
        student = Student.objects.get(id=id)
        return render(request, 'editpage.html', {'student':student})


def delete(request, id):
    student = Student.objects.get(id=id)
    name = Name.objects.get(id=id)
    student.delete()
    name.delete()
    return redirect('/')