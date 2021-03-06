from django.db import models

class Atracao(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    min_age = models.IntegerField()
    photo = models.ImageField(upload_to='atracoes', null=True, blank=True)

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'

    def __str__(self):
        return self.name
