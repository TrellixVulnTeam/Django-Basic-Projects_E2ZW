from django.shortcuts import render
import random
from .models import PasswordReset
from django.conf import settings
from django.core.mail import send_mail



def password(request):
    if request.method == 'POST':
        code = str(random.randint(0, 1000000))
        val = PasswordReset()
        val.res_pass = code
        val.save()

        subject = 'Password Reset Code'
        from_email = settings.EMAIL_HOST_USER
        message = "Hello user, your Shaumik App varification code is: {}\nPlease don't share this code to anyone.".format(code)
        send_to = [[request.POST['email'],]]
        send_mail(subject,message,from_email,send_to)

        msg = 'Code has been sent successfully!'
        return render(request, 'index.html', {'msg':msg})
    else:
        return render(request, 'index.html')