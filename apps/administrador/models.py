from django.db import models

from ..core.models import Usuario
from ..endereco.models import Endereco

# Create your models here.

class Administrador(Usuario):
    nome_completo = models.CharField(verbose_name='Nome', max_length=150)
    endereco = models.ForeignKey(Endereco, models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.is_administrator = True

        if self.pk is None or not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)

        super().save(*args, **kwargs)