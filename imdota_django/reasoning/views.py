from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import Group
from . import models
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from django.core.paginator import Paginator
import json
from django.forms.models import model_to_dict

from reasoning.models import User, Play, Platform
from django.contrib.auth.models import Group
from rest_framework import viewsets
from reasoning.serializers import UserSerializer, PlaySerializer, PlatformSerializer

# Create your views here.

"""
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


def bbsspider(request):
    if request.method == "GET":
        if request.user.is_superuser:

            pageNumber = request.GET.get("index", None)
            if not pageNumber:
                return JsonResponse({"errorCode": "missingParameters"}, status=422)

            r = requests.get('https://www.murdermysterypa.com/plugin.php?id=mini_sjdp:index&page=' + pageNumber)
            soup = BeautifulSoup(r.text, features="html.parser")
            details = soup.find_all('h3', class_="name")

            createdCount = 0

            for detailpage in details:
                title = detailpage.a.text

                isExist = models.Play.objects.filter(name=title).exists()
                if isExist:
                    continue

                subr = requests.get(urljoin("https://www.murdermysterypa.com/", detailpage.a["href"]))
                subsoup = BeautifulSoup(subr.text, features="html.parser")

                litag = subsoup.find(class_="viewsjdpmainul").find_all("li")

                # member number
                memberCount = litag[1].text.split("：")[1]
                memberCount = int("".join(filter(str.isdigit, memberCount)))

                # duration time
                durationTime = litag[3].text.split("：")[1]
                durationTime = int("".join(filter(str.isdigit, durationTime))) * 60

                gradeList = subsoup.find_all(class_="pingjialist")
                reasoningGrade = gradeList[1].find("font").text
                storyGrade = gradeList[2].find("font").text

                play = models.Play(name=title, roleCount=memberCount, durationMinutes=durationTime, reasoningGrade=reasoningGrade, storyGrade=storyGrade)
                play.save()

                # platform
                platform = models.Platform.objects.get(name='线下')
                play.platforms.add(platform)

                createdCount += 1

            return JsonResponse({"message": str(createdCount) + " objects created success"}, status=201)

        else:
            return JsonResponse({"errorCode": "unauthorized"}, status=401)

    else:
        return JsonResponse({"errorCode": "incorrectRequestMethod"}, status=400)


def playlist(request):
    if request.method != "GET":
        return JsonResponse({"errorCode": "incorrectRequestMethod"}, status=400)

    pageNumber = request.GET.get("page", None)
    if not pageNumber:
        return JsonResponse({"errorCode": "missingParameters"}, status=422)

    queryset = models.Play.objects.all()
    paginator = Paginator(queryset, 10)
    plays = paginator.page(pageNumber).object_list

    responseDict = {"data": []}
    for play in plays:
        responseDict["data"].append(model_to_dict(play))

    return JsonResponse(responseDict, status=200)
"""


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
