from django.shortcuts import render, get_object_or_404
from .models import Skill

def homepage(request): #must match urls.py > urlpatterns > path's 2nd argument
    skills = Skill.objects  #django pulls from db
    return render(request, 'skills/home.html', {'skills': skills})

# def roll(request):
#     return render(request, 'skills/roll.html')


def detail(request, skill_id):
    skill_detail = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'skills/detail.html', {'skill': skill_detail})
