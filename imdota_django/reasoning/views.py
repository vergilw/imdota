from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from . import models

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def signin(request):
    if request.method == "GET":
        username = request.GET.get("username", None)
        password = request.GET.get("password", None)
        if username and password:
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
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
                user = models.User(username=username, password=password)
                user.save()
                login(request, user)
                return JsonResponse({"message": "success", "gender": user.gender}, status=200)

        else:
            return JsonResponse({"errorCode": "missingParameters"}, status=422)

    else:
        return JsonResponse({"errorCode": "incorrectRequestMethod"}, status=400)


