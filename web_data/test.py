from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after"
page = urlopen(url)
soup = bs(page, 'html.parser')
print(soup.title)

#댓글 하나 가져와 보기
c_all = soup.find_all("td", class_="title")



# # print(len(c_all))
# # print(c_all[2])
# dat = list(c_all[2].children)

# # dat_comment = dat[6].replace("\n", "")
# # dat_comment = dat_comment.replace("\t","")

# dat_comment = dat[6].strip()

# print(len(dat))
# print(dat_comment)