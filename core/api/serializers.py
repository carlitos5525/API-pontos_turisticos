from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    complete_description = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'name', 'description', 'is_approved', 'photo',
                  'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
                  'complete_description')

    def get_complete_description(self, obj):
        return f'{obj.name} - {obj.description}'
