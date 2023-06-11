from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def LoginPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        pword = request.POST.get('pass')
        
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is wrong")

    return render (request, 'login.html')