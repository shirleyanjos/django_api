from rest_framework import serializers
from core.models import Album, Imagem


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'