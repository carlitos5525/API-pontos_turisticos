from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(is_approved=True)

    # def list(self, request, *args, **kwargs):
        # return Response({'teste': 123})

    # def create(self, request):
        # return Response({'Hello': request.data['nome']})

    # def destroy(self, request, *args, **kwargs):
        # pass

    # criando uma action personalizada
    # detail=True serve para que o framework envie a pk para action
    # endpoint para acessar /pontoturistico/1/denunciar/
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk):
        return Response({'teste': 'deu boa'})
