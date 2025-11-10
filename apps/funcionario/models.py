from django.db import models
from ..pessoa.models import Pessoa
from ..endereco.models import Endereco

# Create your models here.

class Funcionario(Pessoa):
    funcao = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, models.CASCADE, null=True, blank=True)