from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def RegisterPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pword1 = request.POST.get('password1')
        pword2 = request.POST.get('password2')

        if pword1 != pword2:
            messages.error(request, "Your two passwords do not match")
        elif len(pword1) < 6:
            messages.error(request,"Your Password is to short. Use at least 6 Letters")
        elif User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists. Please choose a different username.")

        else:
            my_user = User.objects.create_user(uname,email,pword1)
            my_user.save()
            auth.login(request, my_user)
            return redirect('home')

    return render (request, 'register.html')