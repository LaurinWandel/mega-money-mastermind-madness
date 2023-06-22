"""mastermind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_register.views import RegisterPage
from app_login.views import LoginPage
from app_home.views import HomePage
from app_game.views import GamePage
from app_highscores.views import HighscoresPage
from app_profil.views import ProfilPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RegisterPage, name='register'),
    path('login/',LoginPage, name='login'),
    path('home/',HomePage, name='home'),
    path('game/', GamePage, name='game'),
    path('highscores/', HighscoresPage, name='highscores'),
    path('profil/', ProfilPage, name='profil'),
]
