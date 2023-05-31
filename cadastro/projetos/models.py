# projetos/models.py

from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    integrantes = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=100)
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome
