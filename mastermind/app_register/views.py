from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.

def RegisterPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pword1 = request.POST.get('password1')
        pword2 = request.POST.get('password2')

        if pword1 != pword2:
            return HttpResponse("Your 2 passwords do not match")
        elif len(pword1) < 6:
            return HttpResponse("Your Password is to short. Use at least 6 Letters")

        else:
            my_user = User.objects.create_user(uname,email,pword1)
            my_user.save()
            return redirect('login')

        #print(uname, email, pword1, pword2)

    return render (request, 'register.html')