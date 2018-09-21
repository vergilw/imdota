import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

r = requests.get('https://www.murdermysterypa.com/plugin.php?id=mini_sjdp:index&page=1')
soup = BeautifulSoup(r.text, features="html.parser")
details = soup.find_all('h3', class_="name")
for detailpage in details:
    print(detailpage.a.text)
    subr = requests.get(urljoin("https://www.murdermysterypa.com/", detailpage.a["href"]))
    subsoup = BeautifulSoup(subr.text, features="html.parser")
    # print(subsoup.find(style="padding:10px 0;font-size:15px; "))

    litag = subsoup.find(class_="viewsjdpmainul").find_all("li")

    # member number
    memberCount = litag[1].text.split("：")[1]
    memberCount = int("".join(filter(str.isdigit, memberCount)))

    # duration time
    durationTime = litag[3].text.split("：")[1]
    durationTime = int("".join(filter(str.isdigit, durationTime)))*60

    gradeList = subsoup.find_all(class_="pingjialist")
    reasoningGrade = gradeList[1].find("font").text
    storyGrade = gradeList[2].find("font").text
    print(reasoningGrade, storyGrade)

    break

