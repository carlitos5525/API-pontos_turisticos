from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = ComentarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['comment', 'user__username']
