from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app_game.models import Frage, Antwort
import os


@login_required(login_url='login')
def QuestionPage(request):
    if request.method == 'POST':
        new_question = request.POST['new_question']
        new_answer1 = request.POST['new_answer1']
        new_answer2 = request.POST['new_answer2']
        new_answer3 = request.POST['new_answer3']
        new_answer4 = request.POST['new_answer4']
        answer1_correct = 'answer1_correct' in request.POST
        answer2_correct = 'answer2_correct' in request.POST
        answer3_correct = 'answer3_correct' in request.POST
        answer4_correct = 'answer4_correct' in request.POST

        # Speichern der Frage in der Datenbank
        frage = Frage.objects.create(text=new_question)

        # Speichern der Antworten in der Datenbank
        antwort1 = Antwort.objects.create(frage=frage, text=new_answer1, ist_korrekt=answer1_correct)
        antwort2 = Antwort.objects.create(frage=frage, text=new_answer2, ist_korrekt=answer2_correct)
        antwort3 = Antwort.objects.create(frage=frage, text=new_answer3, ist_korrekt=answer3_correct)
        antwort4 = Antwort.objects.create(frage=frage, text=new_answer4, ist_korrekt=answer4_correct)

        # Speichern der Informationen in das Textdokument
        # Speichern der Informationen in das Textdokument
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'question_user_data.txt')
        with open(file_path, 'a') as file:
            file.write(f"userfrage = Frage.objects.create(text='{new_question}')\n")
            file.write(f"Antwort.objects.create(frage=userfrage, text='{new_answer1}', ist_korrekt={answer1_correct})\n")
            file.write(f"Antwort.objects.create(frage=userfrage, text='{new_answer2}', ist_korrekt={answer2_correct})\n")
            file.write(f"Antwort.objects.create(frage=userfrage, text='{new_answer3}', ist_korrekt={answer3_correct})\n")
            file.write(f"Antwort.objects.create(frage=userfrage, text='{new_answer4}', ist_korrekt={answer4_correct})\n")
            file.write("\n")

        return redirect('home')
    
    return render(request, 'questions.html')