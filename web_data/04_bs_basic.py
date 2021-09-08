from urllib.request import urlopen
from bs4 import BeautifulStoneSoup as bs

url = "https://finance.naver.com/sise/"

page = urlopen(url) #웹 url로부터 페이지를 가져오기
print(page)

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

#
soup = bs(page, features='lxml')
print(soup.title)

#태그명, soup.테그명 => 해당되는 요소의 정보를 가져온다.
print(soup.title)
print(soup.body)
print(soup.div)
print(soup.img)
print(soup.a)

#아이디 클래스를 활용해서 정보가져오기 - 하나의 요소(find)
#아이디 클래스를 활용해서 정보가져오기 - 모든 요소(find_all)
print(soup.find("p", id="p4").text)
for i in soup.find_all("p"):
    print(i.text)

#네이버 정보
#모든 a테그 정보 가져오기

print(soup.find("a"))
print(soup.find_all("a"))

data = soup.find("div")
id_ = data.find("p", id="p4")
print(id_)

#실습
##한줄코드
##class정보를 이용해서 p3인 것을 가져와서 2번째 요소의 text를 가져와보자

print(soup.find_all("p", class_="p3")[1].text)

for i in soup.find_all("a"):
    print(i)

