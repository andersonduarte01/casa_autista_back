from rest_framework import viewsets, permissions
from .models import Funcionario
from .serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('nome_completo')
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        funcionario = serializer.save()
        senha = self.request.data.get('password')
        funcionario.is_funcionario = True
        funcionario.set_password(senha)
        funcionario.save()