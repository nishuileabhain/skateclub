from django.shortcuts import render
from .models import Skill

def homepage(request): #must match urls.py > urlpatterns > path's 2nd argument
    skills = Skill.objects  #django pulls from db
    return render(request, 'skills/home.html', {'skills': skills})

def roll(request):
    return render(request, 'skills/roll.html')
