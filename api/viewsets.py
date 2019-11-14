from rest_framework.viewsets import ModelViewSet
from .serializer import AlbumSerializer, ImagemSerializer
from core.models import Album, Imagem
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly
from django.shortcuts import  get_object_or_404

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ListaAlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class ImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)