
from reasoning.models import User, Play, Platform, Studio, Author, Character, Tag
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'gender')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    play_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Character
        fields = ('id', 'play_id', 'name', 'brief', 'gender')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'gender', 'score')


class PlaySerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    platforms = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    characters = CharacterSerializer(many=True, read_only=True)
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Play
        depth = 1
        # fields = '__all__'
        fields = ('id', 'name', 'brief', 'durationMinutes', 'wordCount', 'publishedDate', 'characterCount', 'isDetective',
                  'isRepresentative', 'logicScore', 'storyScore', 'characters', 'studio', 'author', 'publisher', 'platforms', 'tags')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'name',)


class StudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'






