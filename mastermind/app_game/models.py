from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Frage(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Antwort(models.Model):
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    ist_korrekt = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class Benutzerstand(models.Model):
    benutzername = models.ForeignKey(User, on_delete=models.CASCADE)
    counterstand = models.IntegerField(default=0)

    def __str__(self):
        return f"Benutzer: {self.benutzername.username}, Counterstand: {self.counterstand}"