from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from atracoes.models import Atracao
from .serializers import AtracoesSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']
