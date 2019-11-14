from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    """Um album eh um pacote de imagens, ele tem um titulo e um slug para
    sua identificacao."""

    titulo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo


class Imagem(models.Model):
    """Cada instancia desta classe contem uma imagem da galeria, com seu
    respectivo thumbnail (miniatura) e imagem em tamanho natural.
    Varias imagens podem conter dentro de um Album"""

    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    original = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/original',
    )
    publicacao = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titulo