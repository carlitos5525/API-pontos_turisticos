from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracoesSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer