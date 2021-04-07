from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from rest_framework import serializers

# Serializers define the API representation.
class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'user', 'departamentos', 'empresa', 'total_horas_extra', 'registrohoraextra_set']

