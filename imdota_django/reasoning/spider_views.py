
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import Group
from . import models
import requests, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def spider_bbs(request):
    if request.method == "GET":
        if request.user.is_superuser:

            pageNumber = request.GET.get("index", None)
            if not pageNumber:
                return JsonResponse({"errorCode": "missingParameters"}, status=422)

            r = requests.get('https://www.murdermysterypa.com/plugin.php?id=mini_sjdp:index&page=' + pageNumber, verify=False)
            soup = BeautifulSoup(r.text, features="html.parser")
            details = soup.find_all('h3', class_="name")

            createdCount = 0

            for detailpage in details:
                title = detailpage.a.text

                isExist = models.Play.objects.filter(name=title).exists()
                if isExist:
                    continue

                subr = requests.get(urljoin("https://www.murdermysterypa.com/", detailpage.a["href"]), verify=False)
                subsoup = BeautifulSoup(subr.text, features="html.parser")

                litag = subsoup.find(class_="viewsjdpmainul").find_all("li")

                # member number
                memberCount = litag[1].text.split("：")[1]
                memberCount = int("".join(filter(str.isdigit, memberCount)))

                # duration time
                durationTime = litag[3].text.split("：")[1]
                durationTime = int("".join(filter(str.isdigit, durationTime))) * 60

                scoreList = subsoup.find_all(class_="pingjialist")
                logicScore = scoreList[1].find("font").text
                storyScore = scoreList[2].find("font").text

                play = models.Play(name=title, characterCount=memberCount, durationMinutes=durationTime, logicScore=logicScore, storyScore=storyScore)
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


def spider_baibian(request):
    if not request.user.is_superuser:
        return JsonResponse({"errorCode": "permissionForbidden"}, status=403)

    r = requests.get('https://m.mszmapp.com/playbook/list?alias=publish&page=0&limit=10', verify=False)

    created_count = 0

    for item in r.json()['items']:
        if models.Play.objects.filter(name=item['name']).exists():
            continue

        playScore = item['mark']

        detailRequest = requests.get('https://m.mszmapp.com/playbook/%d/detail' % item['id'], verify=False)
        detailJSON = detailRequest.json()

        play = models.Play(name=detailJSON['name'], characterCount=detailJSON['num_players'], durationMinutes=detailJSON['estimated_time']*60, logicScore=playScore,
                           storyScore=playScore, brief=detailJSON['background'], wordCount=detailJSON['story_text_length'])
        play.save()

        # author
        if not models.Author.objects.filter(name=detailJSON['author']).exists():
            author_request = requests.get('https://m.mszmapp.com/playbook/author?author_id=%d' % detailJSON['author_id'], verify=False)
            author_json = author_request.json()
            author = models.Author(name=author_json['author']['nickname'], brief=author_json['author']['brief'])
            author.save()

        play.author = models.Author.objects.get(name=detailJSON['author'])
        play.save()

        # character
        for character in detailJSON['characters']:
            character_obj = models.Character.objects.get_or_create(name=character['nickname'], brief=character['description'], gender='f' if character['gender']==2 else 'm')[0]
            play.characters.add(character_obj)

        # tag
        playTags = (detailJSON['time'], detailJSON['style'], detailJSON['level'])
        for play_tag in playTags:
            if not models.Tag.objects.filter(name=play_tag).exists():
                tag = models.Tag(name=play_tag)
                tag.save()

            tag = models.Tag.objects.get(name=play_tag)
            play.tags.add(tag)

        # platform
        platform = models.Platform.objects.get(name='百变大侦探')
        play.platforms.add(platform)

        created_count += 1

    return JsonResponse({"message": str(created_count) + " objects created success"}, status=201)


def spider_tiantian(request):
    if not request.user.is_superuser:
        return JsonResponse({"errorCode": "permissionForbidden"}, status=403)

    headers = {'authorization': 'd0f03880-c1fc-11e8-998b-00163e13ebb0'}
    r = requests.get('https://wss.jubensha.xyz/v5/mall/getScriptMallAll/?category=time&pageNo=1', headers=headers, verify=False)

    created_count = 0

    for item in r.json()['list']:
        if models.Play.objects.filter(name=item['name']).exists():
            continue

        payload = {'script_id': item['id']}
        detailRequest = requests.post('https://wss.jubensha.xyz/v5/mall/getScriptMallDetail/', data=payload, headers=headers, verify=False)
        detailJSON = detailRequest.json()

        play = models.Play(name=detailJSON['name'], characterCount=detailJSON['member_number'],
                           logicScore=float(detailJSON['score'])*2, storyScore=float(detailJSON['score'])*2, brief=detailJSON['introduce'])
        play.save()

        # author
        author_obj = models.Author.objects.get_or_create(name='天天剧本杀', brief='天天剧本杀官方App')[0]
        play.author = author_obj
        play.save()

        # character
        for character in detailJSON['characters']:
            character_obj = \
            models.Character.objects.create(name=character['name'], brief=character['character_introduce'])
            play.characters.add(character_obj)

        # tag
        playTags = [detailJSON['subheading']]
        playTags.extend(detailJSON['theme'])
        for play_tag in playTags:
            if not models.Tag.objects.filter(name=play_tag).exists():
                tag = models.Tag(name=play_tag)
                tag.save()

            tag = models.Tag.objects.get(name=play_tag)
            play.tags.add(tag)

        # platform
        platform = models.Platform.objects.get_or_create(name='天天剧本杀')[0]
        play.platforms.add(platform)

        created_count += 1

    return JsonResponse({"message": str(created_count) + " objects created success"}, status=201)


def spider_qu(request):
    if not request.user.is_superuser:
        return JsonResponse({"errorCode": "permissionForbidden"}, status=403)


    r = requests.post('http://www.yiqiwanpai.com/QTL_GAME/Api//fetchPlayList?ctime_msec=0&kind_tag=&role_cnt=&kind_dim=&appid=100801&userid=11740798&timestamp=%d&sign=b1a345151e4077235726c1f3fcc330fd' % int(time.time()),
                      verify=False)

    return HttpResponse(r.text, status=200)