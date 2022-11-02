from rest_framework import viewsets

from portfolio.models import Art
from portfolio.api.serializers import ArtSerializer


class ArtViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing or restrieving arts
    """
    serializer_class = ArtSerializer
    queryset = Art.objects.all()