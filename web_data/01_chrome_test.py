
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

soup = bs(page, 'html.parser')
KOSPI = soup.find("span", id="KOSPI_now")
KOSDAQ = soup.find("span", id="KOSDAQ_now")
KOSPI200 = soup.find("span", id="KPI200_now")
print(KOSPI.text)
print(KOSDAQ.text)
print(KOSPI200.text)

#인기검색
favorite = soup.find("ul", id="popularItemList")
print(favorite.text)

#주요해외
major = soup.find_all('ul', {"class":"lst_major"})
for i in major:
    print(i.text)