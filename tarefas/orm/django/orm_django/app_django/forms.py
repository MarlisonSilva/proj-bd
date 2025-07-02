# app_django/forms.py
from django import forms
from .models import Atividade, Projeto, Funcionario

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao', 'projeto', 'data_inicio', 'data_fim']

class AtualizarLiderForm(forms.Form):
    projeto = forms.ModelChoiceField(queryset=Projeto.objects.all())
    novo_responsavel = forms.ModelChoiceField(queryset=Funcionario.objects.all())

