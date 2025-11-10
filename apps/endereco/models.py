from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=150, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"
