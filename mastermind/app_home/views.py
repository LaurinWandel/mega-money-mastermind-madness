from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')