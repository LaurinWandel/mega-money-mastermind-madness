from django.db import models

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