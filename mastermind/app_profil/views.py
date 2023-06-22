from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def ProfilPage(request):
    user = request.user
    email = user.email
    username = user.username

    if request.method == 'POST':
        if 'update_username' in request.POST:
            new_username = request.POST.get('new_username')
            user.username = new_username
            user.save()
            return redirect('login')

        elif 'delete_user' in request.POST:
            user.delete()
            return redirect('login')

    context = {
        'email': email,
        'username': username
    }

    return render(request, 'profil.html', context)