from selenium import webdriver
from bs4 import BeautifulSoup
import requests



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def geumgang_reserv():
    url = "https://booking.naver.com/booking/13/bizes/780595/items/4665912?theme=place&area=ple"
    data = requests.get(url,headers=headers)


url = "https://booking.naver.com/booking/13/bizes/780595/items/5428141?theme=place&area=ple"
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
#area까지는 css 속성이 접근 가능한데 그 이후부턴 동적이라 selenium 이용해야할듯.

getDays = soup.select('.calendar_area')
print(getDays)
for tr in getDays :
    print('a')
    rank = tr.select_one('.button.calendar_date.unselectable')
    if rank is not None:
        print(rank.text, end=" ")
    title = tr.select_one('button.calendar_date')
    if title is not None:
        print(title.text)
#print(title)
# TODO
# 헤어숍 방향성
# 리퀘스트 받는 것은 여기서 하기.
# 들어가기 이전버튼 까지 만들었으니 스크래핑 해서 언제 가능한지 메뉴 버튼 내리는걸로 생각.
# 눌려진 값을 받아서 아이디 비밀번호 2차 패스워드 받는 값 만들기