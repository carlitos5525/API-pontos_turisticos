from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'line1', 'line2', 'city', 'state',
                  'country', 'latitude', 'longitude')
