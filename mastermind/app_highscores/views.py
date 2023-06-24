from django.shortcuts import render
from app_game.models import Benutzerstand
from django.contrib.auth.decorators import login_required

def convert_counterstand(counterstand):
    conversion_table = {
    1: '0 MYR',
    2: '50 MYR',
    3: '100 MYR',
    4: '200 MYR',
    5: '300 MYR',
    6: '500 MYR',
    7: '1,000 MYR',
    8: '2,000 MYR',
    9: '4,000 MYR',
    10: '8,000 MYR',
    11: '16,000 MYR',
    12: '32,000 MYR',
    13: '64,000 MYR',
    14: '125,000 MYR',
    15: '500,000 MYR',
    16: '1,000,000 MYR',
    17: '2,000,000 MYR',
    18: '4,000,000 MYR',
    19: '8,000,000 MYR',
    20: '16,000,000 MYR',
    21: '32,000,000 MYR',
    22: '64,000,000 MYR',
    23: '125,000,000 MYR',
    24: '250,000,000 MYR',
    25: '500,000,000 MYR',
    26: '1,000,000,000 MYR',
    27: '2,000,000,000 MYR',
    28: '4,000,000,000 MYR',
    29: '8,000,000,000 MYR',
    30: '16,000,000,000 MYR',
    31: '32,000,000,000 MYR',
    32: '64,000,000,000 MYR',
    33: '125,000,000,000 MYR',
    34: '250,000,000,000 MYR',
    35: '500,000,000,000 MYR',
    36: '1,000,000,000,000 MYR',
    37: '2,000,000,000,000 MYR',
    38: '4,000,000,000,000 MYR',
    39: '8,000,000,000,000 MYR',
    40: '16,000,000,000,000 MYR',
    41: '32,000,000,000,000 MYR',
    42: '64,000,000,000,000 MYR',
    43: '125,000,000,000,000 MYR',
    44: '250,000,000,000,000 MYR',
    45: '500,000,000,000,000 MYR',
    46: '1,000,000,000,000,000 MYR',
    47: '2,000,000,000,000,000 MYR',
    48: '4,000,000,000,000,000 MYR',
    49: '8,000,000,000,000,000 MYR',
    50: '16,000,000,000,000,000 MYR',
    51: '32,000,000,000,000,000 MYR',
    52: '64,000,000,000,000,000 MYR',
    53: '125,000,000,000,000,000 MYR',
    54: '250,000,000,000,000,000 MYR',
    55: '500,000,000,000,000,000 MYR',
    56: '1,000,000,000,000,000,000 MYR',
    57: '2,000,000,000,000,000,000 MYR',
    58: '4,000,000,000,000,000,000 MYR',
    59: '8,000,000,000,000,000,000 MYR',
    60: '16,000,000,000,000,000,000 MYR'
    }
    return conversion_table.get(counterstand, 0)  # Rückgabe von 0, falls der Wert nicht in der Tabelle vorhanden ist

@login_required(login_url='login')
def HighscoresPage(request):
    top_10 = Benutzerstand.objects.order_by('-counterstand')[:10]
    converted_top_10 = [(convert_counterstand(bs.counterstand), bs.benutzername) for bs in top_10]
    context = {'top_10': converted_top_10}
    return render(request, 'highscores.html', context)
