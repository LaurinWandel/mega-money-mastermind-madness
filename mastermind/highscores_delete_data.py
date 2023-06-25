import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mastermind.settings')

django.setup()

from app_game.models import Benutzerstand

def delete_highscores():
    Benutzerstand.objects.all().delete()


    print("Daten erfolgreich gelöscht.")

delete_highscores()