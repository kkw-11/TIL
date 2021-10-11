import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/jun/Downloads/chromedriver')

_input = input('test')
url = f"https://map.naver.com/v5/search/{_input}"
driver.get(url)
test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '''_pcmap_list_scroll_container''')))
print(test)
def crawling(soup) :
    space = soup.find("div", class_= "place_section no_margin")
    result=[]
    for div in space.find_all("li"):
        result.append(div.get_text())
    return result
    
def main() :
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(crawling(soup))


if __name__ == "__main__" :
    main()