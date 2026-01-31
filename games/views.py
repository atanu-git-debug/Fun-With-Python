from django.shortcuts import render
from . models import Game
from Game import guessing
# Create your views here.
def play(request,pk):
    game = Game.objects.filter(pk=pk)
    if game == 'guess':
        return render(request,'game/guess.html')
    