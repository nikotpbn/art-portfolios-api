from rest_framework import serializers
from portfolio import models


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
            model = models.Art
            fields = '__all__'
            read_only_fields = ['id']