#코스닥 정보에 대한
#지수 정보 20210908_14_index.csv
#시황정보 뉴스 20210908_14_news.csv
#시황정보 리포트 2010908_14_report.csv
#인기검색어 20210908_14_top_word.csv
#가장 많이 본 뉴스 20210908_14_cnt_news.csv

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time
import pandas as pd

#파일쓰기 함수
def file_write(col, data):
    dat = pd.DataFrame({col : data})
    filename = tt + "_" + col + "_" + ".csv"
    dat.to_csv(filename, index=False)
    return 0

#시간 설정
total_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
now_time = time.strftime('%c', time.localtime(time.time()))
tt = time.strftime('%Y%m%d', time.localtime(time.time()))


#사이트 불러오기 / 파싱
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = bs(page, 'lxml')


#지수정보
index_info = soup.find("em", id="now_value")
# print(total_time + " [코스닥지수] : " + index_info.text)
file_write("지수정보", index_info)
