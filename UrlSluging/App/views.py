from django.shortcuts import render, redirect
from App.models import Student


def home(request):
    template_name = "home.html"
    if request.method == "POST":
        std = Student()
        std.title = request.POST['title']
        std.save()
        return  redirect('home')
    else:
        std = Student.objects.all()
        return render(request, template_name, {"std":std})


def details(request, slug, id):
    template_name = "details.html"
    std = Student.objects.get(slug=slug, id=id)

    return render(request, template_name, {"std":std})
