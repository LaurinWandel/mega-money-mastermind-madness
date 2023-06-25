from django.shortcuts import render, redirect
from .models import Frage, Antwort, Benutzerstand
import random
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def GamePage(request):
    fragen = Frage.objects.all()
    aktuelle_frage = None
    ist_korrekt = None

    # Init counter
    if 'counter' not in request.session:
        request.session['counter'] = 1

     # Get IDs of answered questions from session
    beantwortete_fragen_ids = request.session.get('beantwortete_fragen_ids', [])


    if request.method == 'POST':
        antwort_id = request.POST.get('antwort')
        antwort = Antwort.objects.get(id=antwort_id)
        ist_korrekt = antwort.ist_korrekt
        
        # reset counter if awnser wrong
        if not ist_korrekt:
            if request.user.is_authenticated:
                benutzerstand = Benutzerstand.objects.create(
                    benutzername=request.user,
                    counterstand=request.session['counter']
                )
                benutzerstand.save()
            request.session['counter'] = 0
            
        request.session['counter'] += 1

        print (request.session['counter'])

        # Add answered question ID to the list in session
        beantwortete_fragen_ids.append(antwort.frage.id)
        request.session['beantwortete_fragen_ids'] = beantwortete_fragen_ids

    # Exclude answered questions from the queryset
    unbeantwortete_fragen = fragen.exclude(id__in=beantwortete_fragen_ids)
    print(unbeantwortete_fragen)
    print(len(unbeantwortete_fragen))

    if not unbeantwortete_fragen:
        # Reset the answered questions list
        beantwortete_fragen_ids = []
        request.session['beantwortete_fragen_ids'] = beantwortete_fragen_ids

        # Add all questions to unanswered questions
        unbeantwortete_fragen = fragen

    if unbeantwortete_fragen:
        # Eine zufällige unbeantwortete Frage auswählen
        aktuelle_frage = random.choice(unbeantwortete_fragen)

    return render(request, 'game.html', {'aktuelle_frage': aktuelle_frage, 'ist_korrekt': ist_korrekt, 'counter': request.session['counter']})