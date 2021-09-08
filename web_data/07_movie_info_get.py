from bs4 import BeautifulSoup
from urllib.request import urlopen


#url정보
#tag, id, class 정보확인

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
# print(soup.title)

# 제목 - 하나 성공
# tit_data = soup.find("dt", class_="tit").find("a").text
# print(tit_data)

# 제목 - 하나 성공
tit_all_data = soup.find_all("dt", class_="tit")

list_all = []
for one in tit_all_data:
    title_one = one.find("a").text
    list_all.append(title_one)
print(len(list_all), list_all)

# 평점 점수 가져오기
#
score_all = soup.find_all("span", class_='num')
print(score_all[1].text)

# 평점가져오기
score_all = soup.find_all("dl", class_='info_star')
# print( score_all[0].find("span", class_='num').text )

all_score = []
for one in score_all:
    one_score = one.find("span", class_="num").text
    all_score.append(one_score)
print(all_score)



#예매율 정보 가져오기
rate_tmp = soup.find_all("div", class_='star_t1 b_star')
# print( score_all[0].find("span", class_='num').text )

rate_all_score = []
for one in rate_tmp:
    one_score = one.find("span", class_="num").text
    rate_all_score.append(one_score)
print(len(rate_all_score),rate_all_score)

#참여 인원 가져오기
pp = soup.find_all("dl", class_="info_star")
pp_all = []
for i in pp:
    pp = i.find("em").text
    pp_all.append(pp)
print(pp_all)


#지금까지 얻은 정보
#타이틀, 평점, 예매율, 참여인원

#개요 정보 가져오기
# outline = soup.find_all("span", class_="link_txt")


#데이터 모으기
import pandas as pd

dict_dat = {"영화제목":list_all,
            "평점": all_score,
            "평점 참여명수": pp_all }
dat = pd.DataFrame(dict_dat)
print(dat)
dat.to_csv("naver_movie_info.csv", index=True)
dat.to_excel("naver_movie_info.xlsx", index=False)