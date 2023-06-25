from django.contrib import admin
from app_game.models import Frage, Antwort, Benutzerstand

# Register your models here.

admin.site.register(Benutzerstand)
admin.site.register(Frage)
admin.site.register(Antwort)
