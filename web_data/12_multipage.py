
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import time

# page = urlopen(basic_url)
# soup = bs(page, 'html.parser')
# print(soup.title)


comments = []

for i in range(1,51,1):
    basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page="
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = bs(page, 'html.parser')
    comment_all = soup.find_all("td", class_="title")
    print(len(comment_all))

    
    for one in comment_all:
        temp = list(one.children)[6].strip()
        # print(temp)
        comments.append(temp)
    time.sleep(0.1)

print(comments)

dict_dat = { "영화댓글" : comments}
dat = pd.DataFrame(dict_dat)

# print(dat)

dat.to_csv("댓글_멀티페이지.csv", index=False)
dat.to_excel("댓글_멀티페이지.xlsx", index = False)


