from django.shortcuts import render
from .models import Clinica

def lista_clinicas(request):
    clinicas = Clinica.objects.all()
    return render(request, 'agendamentos/lista_clinicas.html', {'clinicas': clinicas})

def home(request):
    return render(request, 'agendamentos/home.html')