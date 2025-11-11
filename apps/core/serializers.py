from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # O Django espera 'username', mesmo que seu USERNAME_FIELD seja 'email'
        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError({"detail": "Credenciais inválidas."})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "Usuário inativo."})

        refresh = RefreshToken.for_user(user)

        if user.is_administrator:
            painel = "/painel/admin/"
            tipo = "administrador"
        elif user.is_funcionario:
            painel = "/painel/funcionario/"
            tipo = "funcionario"
        elif user.is_profissional:
            painel = "/painel/profissional/"
            tipo = "profissional"
        elif user.is_responsavel:
            painel = "/painel/responsavel/"
            tipo = "responsavel"
        else:
            painel = "/painel/"
            tipo = "usuario"

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "nome": user.nome,
                "tipo": tipo,
                "painel_url": painel,
            }
        }
