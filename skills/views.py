from django.shortcuts import render


def roll(request):
    return render(request, 'skills/roll.html')
