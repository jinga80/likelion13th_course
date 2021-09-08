from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = bs(page, 'lxml')
print(soup.title)

#코스피 정보 가져오기
kospi_info = soup.find("em", id="now_value")
print(kospi_info.text)

#거래량 천주 정보 가져오기
deal_info = soup.find("td", id="quant")
print("거래량: ", deal_info.text)

#거래량 장중최고 
deal_info = soup.find("td", id="high_value")
print("거래량: ", deal_info.text)

#거래량 52주최고
deal_info = soup.find_all("td", class_="td")[2]
print("거래량: ", deal_info.text)

#투자자별 매매동향, 프로그램 매매동향- 댓글
deal_info = soup.find("dl", class_="lst_kos_info")
print(deal_info.text)


#실습 - 시황뉴스
deal_info = soup.find_all("span", class_= "tit")
news = []
for name, i in enumerate(deal_info):
    news.append(i.text)
    # print(name, i)

for i in news[0:5]:
    print("시황뉴스 : " + i )

print("\n")
#(추가)시황정보 리포트 정보 가져오기 - 댓글 
deal_info = soup.find_all("span", class_= "tit")
news_info = []
for name, i in enumerate(deal_info):
    news_info.append(i.text)
    # print(name, i)

for i in news_info[5:]:
    print("시황정보 리포트 : " + i)

# no 코스피정보, 거래량(천주), 장중최고, 52주최고, 시황뉴스
# 1, -------, ---------,  ----,  ------,  -----

#시황뉴스 목록을 csv 파일로 만들기
import pandas as pd

dat = pd.DataFrame({"시황뉴스" : news})
print(dat)
dat.to_csv("news.csv", index=False)
dat.to_excel("news.xlsx", index=False)