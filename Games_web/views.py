
from django.shortcuts import render

from games.models import Game


def home(request):
    games = Game.objects.all()
    
    context={
        'games': games
    }
    return render(request, 'home.html', context)