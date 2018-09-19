import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

r = requests.get('https://www.murdermysterypa.com/plugin.php?id=mini_sjdp:index&page=1')
soup = BeautifulSoup(r.text, features="html.parser")
details = soup.find_all('h3', class_="name")
for detailpage in details:
    print(detailpage.a["href"])
    subr = requests.get(urljoin("https://www.murdermysterypa.com/", detailpage.a["href"]))
    subsoup = BeautifulSoup(subr.text, features="html.parser")
    print(subsoup.find(style="padding:10px 0;font-size:15px; "))
    # break

