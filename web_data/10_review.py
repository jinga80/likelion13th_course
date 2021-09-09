from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd

url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after"
page = urlopen(url)
soup = bs(page, 'html.parser')
print(soup.title)

#댓글 하나 가져와 보기
c_all = soup.find_all("td", class_="title")
# print(len(c_all))
# print(c_all[2])
dat = list(c_all[2].children)

# dat_comment = dat[6].replace("\n", "")
# dat_comment = dat_comment.replace("\t","")

dat_comment = dat[6].strip()

print(len(dat))
print(dat_comment)

#댓글 1페이지의 댓글 전체 가져오기
comments = []

for i in range(1,3):
    url1 = f"https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page={i}"
    page = urlopen(url1)
    soup = bs(page, "html.parser")
    commet_all = soup.find_all("td", class_="title")
    # print(len(commet_all))

    for one in commet_all:
        temp = list(one.children)[6].strip()
        # print(temp)
        comments.append(temp)


print(comments)

dict_dat = { "영화댓글" : comments}
dat = pd.DataFrame(dict_dat)

print(dat)

dat.to_csv("댓글.csv", index=False)
dat.to_excel("댓글.xlsx", index = False)

