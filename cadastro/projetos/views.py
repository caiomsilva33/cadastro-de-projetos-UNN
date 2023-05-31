from django.shortcuts import render, redirect
from .forms import ProjetoForm
from .models import Projeto


def home(request):
    return render(request, 'home.html')

def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'cadastro_projeto.html', {'form': form})

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista_projetos.html', {'projetos': projetos})