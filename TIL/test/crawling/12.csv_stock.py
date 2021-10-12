import csv
import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf8",newline="")
writer = csv.writer(f)

for page in range(1,2):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        colums = row.find_all("td")
        if len(colums) <= 1:
            continue
        data = [column.get_text().strip() for column in colums]
        # print(data)
        writer.writerow(data)