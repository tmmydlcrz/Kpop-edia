from rest_framework import serializers
from .models import Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)  # Nested serializer

    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = '__all__'
