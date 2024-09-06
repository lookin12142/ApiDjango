from rest_framework import serializers

class OriginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    url = serializers.URLField()

class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    url = serializers.URLField()

class CharacterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=100)
    species = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100, allow_blank=True)
    gender = serializers.CharField(max_length=100)
    origin = OriginSerializer()
    location = LocationSerializer()
    image = serializers.URLField()
    episode = serializers.ListField(child=serializers.URLField())
    url = serializers.URLField()

class InfoSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    pages = serializers.IntegerField()
    next = serializers.URLField(allow_null=True)
    prev = serializers.URLField(allow_null=True)

class ApiResponseSerializer(serializers.Serializer):
    info = InfoSerializer()
    results = CharacterSerializer(many=True)
