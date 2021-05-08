from autoslug import AutoSlugField #instalado de terceiros
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel #instalado de terceiros (cria data de criação em alteração)

class Marcador(models.Model):
    nome =  models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome