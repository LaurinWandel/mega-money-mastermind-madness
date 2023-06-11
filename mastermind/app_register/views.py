from django.shortcuts import render

# Create your views here.
def RegisterPage(request):
    return render (request, 'register.html')

def LoginPage(request):
    return render (request, 'login.html')

def HomePage(request):
    return render (request, 'home.html')