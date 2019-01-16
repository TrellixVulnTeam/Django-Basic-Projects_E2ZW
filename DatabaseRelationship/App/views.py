from django.shortcuts import render, redirect
from .models import Garden, Flower

def index(request):
    if request.method == "POST":
        garden = Garden()
        garden.name = request.POST['garden_name']
        garden.description = request.POST['garden_desc']
        garden.save()

        return redirect('/')
    else:
        return render(request, 'index.html')


def index2(request):
    if request.method == "POST":
        flower = Flower()
        flower.name = request.POST['flower_name']
        flower.color = request.POST['flower_color']
        flower.description = request.POST['flower_desc']
        flower.garden = Garden.objects.get(id=int(request.POST['gid']))
        flower.save()
        return redirect('/index2/')
    else:
        garden = Garden.objects.all()
        return render(request, 'index2.html', {'garden':garden})