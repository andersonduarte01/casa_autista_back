from ..core.models import Usuario
from django.db import models

class Pessoa(Usuario):
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome_completo



