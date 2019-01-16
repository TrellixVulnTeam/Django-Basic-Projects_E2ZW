from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from  .models import Student
from django.db.models import Q



def add_student(request):
    if request.method == "GET":
        return render(request, 'add_student.html')
    else:
        student = Student()
        student.name = request.POST['stname']
        student.roll = request.POST['stroll']
        student.st_class = request.POST['stclass']
        student.department = request.POST['stdepartment']
        student.save()

        return redirect('/student_list/')


def student_list(request):
    student = Student.objects.all()
    paginator = Paginator(student, 2)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'student_list.html', {'student':contacts})




def search(request):
    if request.method == "GET":
        return render(request, 'search.html')
    else:
        search = request.POST['srch']

        if search:
            match = Student.objects.filter(
                Q(name__contains=search) | Q(roll__contains=search) | Q(st_class__contains=search) | Q(
                    department__contains=search))
            if match:
                return render(request, 'search.html', {'result': match})
            else:
                error = 'No result found'
                return render(request, 'search.html', {'error': error})