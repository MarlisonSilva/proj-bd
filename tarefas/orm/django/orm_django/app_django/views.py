from django.shortcuts import render, redirect
from .forms import AtividadeForm, AtualizarLiderForm
from .models import Projeto

def adicionar_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = AtividadeForm()
    return render(request, 'telas/adicionar_atividade.html', {'form': form})
    
def atualizar_lider(request):
    if request.method == 'POST':
        form = AtualizarLiderForm(request.POST)
        if form.is_valid():
            projeto = form.cleaned_data['projeto']
            novo_responsavel = form.cleaned_data['novo_responsavel']
            projeto.responsavel = novo_responsavel
            projeto.save()
            return redirect('listar_projetos')
    else:
        form = AtualizarLiderForm()
    return render(request, 'telas/atualizar_lider.html', {'form': form})

def listar_projetos(request):
    projetos = Projeto.objects.all().prefetch_related('atividade_set')
    return render(request, 'telas/listar_projetos.html', {'projetos': projetos})

def home(request):
    return render(request, 'telas/tela_inicial.html')