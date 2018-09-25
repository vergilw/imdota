
from reasoning.models import User, Play, Platform, Studio, Author, Role, Tag
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'gender', 'groups')


class PlaySerializer(serializers.HyperlinkedModelSerializer):
    # platforms = serializers.HyperlinkedRelatedField(many=True, view_name='platform-detail',
    #  lookup_field='name', read_only=True)

    class Meta:
        model = Play
        depth = 1
        fields = '__all__'
        # fields = ('id', 'name', 'brief', 'durationMinutes', 'publishedDate', 'roleCount', 'isDetective',
        #           'isRepresentative', 'reasoningGrade', 'storyGrade', 'studio', 'author', 'publisher', 'platforms')


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


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
