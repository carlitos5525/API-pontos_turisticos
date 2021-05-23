from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    # lookup_field serve para modificar o endpoint atracoes/1/ para buscar pelo atributo que eu informar
    # lookup_field = 'user'
