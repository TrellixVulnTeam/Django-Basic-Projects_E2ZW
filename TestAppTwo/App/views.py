from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'index.html')