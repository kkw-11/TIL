import requests
from requests.api import head
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
url = "https://map.naver.com/v5/"
res = requests.get(url,headers=headers)
res.raise_for_status()

with open("mapnamver.html","w",encoding="utf8") as f :
    f.write(res.text)