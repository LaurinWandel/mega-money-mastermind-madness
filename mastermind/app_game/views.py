from django.shortcuts import render, redirect
from .models import Frage, Antwort, Benutzerstand
import random

def GamePage(request):
    fragen = Frage.objects.all()
    aktuelle_frage = None
    ist_korrekt = None

    # Initialisierung des Zählers
    if 'counter' not in request.session:
        request.session['counter'] = 1

    if request.method == 'POST':
        antwort_id = request.POST.get('antwort')
        antwort = Antwort.objects.get(id=antwort_id)
        ist_korrekt = antwort.ist_korrekt
        
        # Wenn die Antwort falsch ist, setze den Zähler zurück
        if not ist_korrekt:
            if request.user.is_authenticated:
                benutzerstand = Benutzerstand.objects.create(
                    benutzername=request.user,
                    counterstand=request.session['counter']
                )
                benutzerstand.save()
            request.session['counter'] = 0
            benutzerstaende = Benutzerstand.objects.all()
            for eintrag in benutzerstaende:
                print(f"Benutzername: {eintrag.benutzername.username}, Counterstand: {eintrag.counterstand}")

        request.session['counter'] += 1

        print (request.session['counter'])

    # Alle Fragen außer bereits beantworteten Fragen abrufen
    unbeantwortete_fragen = fragen.exclude(id__in=[frage.id for frage in fragen if frage == aktuelle_frage])

    if unbeantwortete_fragen:
        # Eine zufällige unbeantwortete Frage auswählen
        aktuelle_frage = random.choice(unbeantwortete_fragen)

    return render(request, 'game.html', {'aktuelle_frage': aktuelle_frage, 'ist_korrekt': ist_korrekt, 'counter': request.session['counter']})