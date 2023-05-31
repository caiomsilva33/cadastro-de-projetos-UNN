# projetos/forms.py

from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'integrantes', 'responsavel', 'data_inicio']
