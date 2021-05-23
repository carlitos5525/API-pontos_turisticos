from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # lookup_field serve para modificar o endpoint atracoes/1/ para buscar pelo atributo que eu informar
    # lookup_field = 'user'
