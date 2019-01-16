from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from App.models import Employee


def user_login(request):
    if request.method == "POST":
        au = request.POST['au']
        password = request.POST['password']
        user = authenticate(request,username=au, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid"
            return render(request, 'login.html', {'error':error})
    else:
        return render(request, 'login.html')


def dashboard(request):
    data = request.user
    return render(request, 'dashboard.html', {'data':data})



def user_logout(request):
    logout(request)
    return redirect('login')