
from reasoning.models import User, Play, Platform, Studio, Author, Role, Tag
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'gender')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    play_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Role
        fields = ('id', 'play_id', 'name', 'brief', 'gender')


class PlaySerializer(serializers.HyperlinkedModelSerializer):
    platforms = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        depth = 1
        # fields = '__all__'
        fields = ('id', 'name', 'brief', 'durationMinutes', 'wordCount', 'publishedDate', 'roleCount', 'isDetective',
                  'isRepresentative', 'logicScore', 'storyScore', 'roles', 'studio', 'author', 'publisher', 'platforms')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'name',)


class StudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
