
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd


# page = urlopen(basic_url)
# soup = bs(page, 'html.parser')
# print(soup.title)


comments = []

for i in range(1,6,1):
    basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=185614&target=after&page="
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = bs(page, 'html.parser')
    comment_all = soup.find_all("td", class_="title")
    print(len(comment_all))

    
    for one in comment_all:
        temp = list(one.children)[6].strip()
        # print(temp)
        comments.append(temp)


print(comments)

dict_dat = { "영화댓글" : comments}
dat = pd.DataFrame(dict_dat)

# print(dat)

dat.to_csv("다른영화댓글.csv", index=False)
dat.to_excel("다른영화댓글.xlsx", index = False)


