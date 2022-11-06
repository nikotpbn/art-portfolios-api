from rest_framework import serializers
from portfolio import models


class ArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Art
        fields = ['id', 'title', 'subtitle', 'image', 'description', 'type']
        read_only_fields = ['id']


class ArtImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Art
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}