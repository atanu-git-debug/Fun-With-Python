from django.shortcuts import render
from django.http import HttpResponse
from . models import Game
from Game import guessing
# Create your views here.
def play(request,pk):
    game = Game.objects.get(pk=pk)
    game_name = game.name
    print(game_name)
    context = {
        'game' : game,
        'game_name' : game_name
    }
    
    return render(request,f'game/{game_name}.html', context)

