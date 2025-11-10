from rest_framework import serializers
from .models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Funcionario
        fields = [
            'id',
            'email',
            'password',
            'nome_completo',
            'cpf',
            'data_nascimento',
            'telefone',
            'funcao',
            'data_criacao',
            'data_atualizacao',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        funcionario = Funcionario(**validated_data)
        if password:
            funcionario.set_password(password)  # hash seguro
        funcionario.save()
        return funcionario

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # hash seguro
        instance.save()
        return instance