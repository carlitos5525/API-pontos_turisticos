from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    enderecos = EnderecoSerializer()
    complete_description = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'name', 'description', 'is_approved', 'photo',
                  'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
                  'complete_description')

        # read_only_fields = ('comentarios', 'avaliacoes', 'enderecos')

    def create_atracoes(selfself, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        endereco = validated_data['enderecos']
        del validated_data['enderecos']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.create_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.enderecos = end
        ponto.save()
        return ponto


    @staticmethod
    def get_complete_description(obj):
        return f'{obj.name} - {obj.description}'
