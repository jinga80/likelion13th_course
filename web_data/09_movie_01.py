from bs4 import BeautifulSoup
from urllib.request import urlopen

#웹페이지 소스 가져오기 및 파싱
url = "http://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

print(soup.title)


##상영작 / 예정작 제목만 뽑기
soup_ul_li = soup.find("ul", class_='lst_detail_t1').find_all('li')
print(len(soup_ul_li))
print(soup_ul_li[122].find("dt",class_="tit").a.text)


#평점
print(soup_ul_li[4].find("span", class_="num").text)

#참여인원
print(soup_ul_li[0].find("em").text)

#예매율
temp = soup_ul_li[122].find("dl",class_="info_exp")
if temp is not None:
    t = temp.span.text
    print("값이있음",t)
else:
    t = 0
    print("값이없음",t)
# print(soup_ul_li[122].find("dl",class_="info_exp").span.text)

#개요
txt = soup_ul_li[0].find("span", class_="link_txt").text
txt_last = txt.replace("\n","")
txt_last = txt_last.replace("\t","")
txt_last = txt_last.replace("\r","")
print(txt_last)

#감독
coach_txt = soup_ul_li[0].find("span", class_="link_txt").find("a").text
coach = coach_txt.replace("\n","")
coach = coach.replace("\t","")
coach = coach.replace("\r","")
print(coach)


#제목, 평점, 참여수, 개요
all_title = []
all_score = []
all_people = []
all_rate = []
all_catagory = []

for one in soup_ul_li:
    title = one.find("dt",class_="tit").a.text
    score = one.find("span", class_="num").text
    num_people = one.find("em").text
    
    #예매율
    tmp = one.find("dl", class_="info_exp")
    if tmp is not None:
        rate = tmp.span.text
    else:
        rate = 0

    category = one.find("span", class_="link_txt").text

    txt_last = txt.replace("\n","")
    txt_last = txt_last.replace("\t","")
    txt_last = txt_last.replace("\r","")

    all_title.append(title)
    all_score.append(score)
    all_people.append(num_people)
    all_rate.append(rate)
    all_catagory.append(txt_last)

print(len(all_title),len(all_score),len(all_people),len(all_catagory))

#저장을 위한 csv, xlsx파일 만들기
import pandas as pd

dat_dict = {
    "제목" : all_title,
    "평점" : all_score,
    "참여명수" : all_people,
    "예매율" : all_rate,
    "개요" : all_catagory
}
dat = pd.DataFrame(dat_dict)
dat.to_csv("네이버영화.csv", index=False)
dat.to_excel("네이버영화.xlsx", index=False)



#기타 정보(감독, 출연, 상영시간)추가
#개봉 날짜 추가
#감독 인원 추가