from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['comment', 'user__username']
