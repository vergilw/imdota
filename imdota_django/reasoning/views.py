
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import Group
from . import models
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from reasoning.models import User, Play, Platform, Studio, Author, Character, Tag
from rest_framework import viewsets
from reasoning.serializers import UserSerializer, PlaySerializer, PlatformSerializer, StudioSerializer, AuthorSerializer, CharacterSerializer, TagSerializer

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. web hooks ")


def signin(request):
    if request.method == "GET":
        username = request.GET.get("username", None)
        password = request.GET.get("password", None)
        if username and password:
            try:
                user = models.User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return JsonResponse({"message": "success", "gender": user.gender}, status=200)
                else:
                    return JsonResponse({"errorCode": "incorrectPassword"}, status=400)
            except:
                return JsonResponse({"errorCode": "userNotFound"}, status=400)

        else:
            return JsonResponse({"errorCode": "missingParameters"}, status=422)

    else:
        return JsonResponse({"errorCode": "incorrectRequestMethod"}, status=400)


def signup(request):
    if request.method == "GET":
        username = request.GET.get("username", None)
        password = request.GET.get("password", None)
        if username and password:
            try:
                models.User.objects.get(username=username)
                return JsonResponse({"errorCode": "userAlreadyExist"}, status=400)

            except:
                user = models.User(username=username)
                user.set_password(password)
                user.save()
                login(request, user)
                return JsonResponse({"message": "success", "gender": user.gender}, status=200)

        else:
            return JsonResponse({"errorCode": "missingParameters"}, status=422)

    else:
        return JsonResponse({"errorCode": "incorrectRequestMethod"}, status=400)


def createeditor(request):
    if request.method == "GET":
        if request.user.is_superuser:
            username = request.GET.get("username", None)
            password = request.GET.get("password", None)
            if username and password:
                try:
                    models.User.objects.get(username=username)
                    return JsonResponse({"errorCode": "userAlreadyExist"}, status=400)

                except:
                    user = models.User(username=username)
                    user.set_password(password)
                    user.is_staff = True
                    user.save()
                    editorGroup = Group.objects.get(name='editor')
                    editorGroup.user_set.add(user)
                    return JsonResponse({"message": "created success"}, status=201)

            else:
                return JsonResponse({"errorCode": "missingParameters"}, status=422)

        else:
            return JsonResponse({"errorCode": "unauthorized"}, status=401)

    else:
        return JsonResponse({"errorCode": "incorrectRequestMethod"}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PlayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class StudioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
