import urllib.request 
import requests, json
from bs4 import BeautifulSoup
from requests.api import request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_address():
    url = "https://map.naver.com/v5/search/흑다우"
    # place = "흑다우"
    # url = url + place

    req = requests.get(url)
    print(req.status_code)
    soup = BeautifulSoup(req.text, "html.parser")
    time.sleep(5)
    div_tag = soup.find("body",attrs={"class":"place_on_pcmap"})
    print(div_tag)

    # print(div_tag.find("a").text)

if __name__ == "__main__" :
    # find_restaurant()
    find_address()
    # open_api()