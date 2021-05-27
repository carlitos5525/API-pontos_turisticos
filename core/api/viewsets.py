from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        query = PontoTuristico.objects.filter(is_approved=True)
        if id:
            query = query.filter(id=id)
        if name:
            query = query.filter(name__icontains=name)
        if description:
            query = query.filter(description=description)
        return query

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

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpResponse('Ok')
