import os
import django

# Setze die Umgebungsvariable "DJANGO_SETTINGS_MODULE" auf das Modul, das deine Django-Einstellungen enthält
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mastermind.settings')

# Lade die Django-Einstellungen
django.setup()

# Importiere das Modell, das du verwenden möchtest
from app_game.models import Frage, Antwort

def delete_questions():
    # Lösche alle Fragen und Antworten aus der Datenbank
    Frage.objects.all().delete()
    Antwort.objects.all().delete()

    print("Daten erfolgreich gelöscht.")

# Führe die Funktion aus, um die Daten zu löschen
delete_questions()