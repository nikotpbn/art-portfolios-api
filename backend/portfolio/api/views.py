from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from portfolio.models import Art
from portfolio.api.serializers import (
        ArtSerializer,
        ArtImageSerializer
    )


class ArtViewSet(viewsets.ModelViewSet):
    """
    List of Arts
    Retrieve single art
    """
    serializer_class = ArtSerializer
    queryset = Art.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.action == 'list':
            return ArtSerializer
        elif self.action == 'upload_image':
            return ArtImageSerializer
        else:
            return ArtSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
