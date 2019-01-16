from django.shortcuts import render, redirect
from django.contrib import messages
from MyApp.forms import PasswordForm
from MyApp.models import PasswordModel



'''def home(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            confirm_password = form.cleaned_data['confirm_password']
            PasswordModel.objects.create(password=confirm_password)
            messages.success(request,"Password has been saved successfully")
            return redirect('home')
        else:
            form = PasswordForm()
            return render(request, 'index.html', {'form':form})
    else:
        form = PasswordForm()
        return render(request, 'index.html', {'form':form})'''

def home(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'index.html')
        else:
           print(form.errors) #To see the form errors in the console.
    else:
        form = PasswordForm()
    # If form is not valid, this would re-render inputtest.html with the errors in the form.
    return render(request, 'index.html', {'form': form})