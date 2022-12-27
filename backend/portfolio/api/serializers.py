from rest_framework import serializers
from portfolio import models

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = ['name']

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Artist
        exclude = ['id']

class ArtSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    tags = serializers.StringRelatedField(many=True)
    artists = ArtistSerializer()

    class Meta:
        model = models.Art
        fields = ['id', 'title', 'subtitle', 'image', 'description', 'type', 'created_at', 'tags', 'artists']
        read_only_fields = ['id']


class ArtImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Art
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}