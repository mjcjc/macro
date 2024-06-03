from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# TODO
# 헤어숍 방향성
# 리퀘스트 받는 것은 여기서 하기.
# 순서도/ 날짜 클릭 -> 시간 클릭 -> 맞춤컷 클릭-> 결제버튼 누르면 -> 아이디 비번 확인.
# 눌려진 값을 받아서 아이디 비밀번호 2차 패스워드 받는 값 만들기
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options) # 크롬 드라이버의 경로를 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

#일준 
#def iljunHair():
url = "https://booking.naver.com/booking/13/bizes/780595/items/5428141?theme=place&area=ple"
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
driver.get(url)
#return driver.get(url)

#금강
def geumgang_reserv():
    url = "https://booking.naver.com/booking/13/bizes/780595/items/4665912?theme=place&area=ple"
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    return driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
getDays = soup.select('#root > main > section.section_calendar > div > div.section_content > div.calendar_area > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > button')
#element 값에서 calendar_date 값만 있는 걸 가져와서 예약이 가능한 걸 저장해주는 변수가 필요함
#지금 조건문에서 발동은 하는데 문제는 값이 다 들어가서 조건문의 조건을 다시 작성해야함.
dates = []
for i in range(1,7):
    for j in range(1,8):
        selector = f'#root > main > section.section_calendar > div > div.section_content > div.calendar_area > div > table > tbody > tr:nth-child({i}) > td:nth-child({j}) > button.calendar_date'
        elements = soup.select(selector)
        for element in elements:
            # calendar_date 클래스를 가진 요소만을 선택하고, unselectable 클래스를 가지지 않는 요소만을 선택합니다.
            if 'calendar_date' in element.get('class', []) and 'unselectable' not in element.get('class', []):
                date = element.find('span', class_='num').text
                dates.append(date)
                print(date)

driver.quit()


