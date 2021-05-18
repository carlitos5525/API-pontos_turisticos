from django.db import models
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from atracoes.models import Atracao
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'

    def __str__(self):
        return self.name
