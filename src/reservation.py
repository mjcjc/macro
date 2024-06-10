from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options) # 크롬 드라이버의 경로를 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = "https://booking.naver.com/booking/13/bizes/780595/items/5428141?theme=place&area=ple"
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
driver.get(url)


time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

dates = []
times = []
#날짜에 따라 예약 가능한 값 넣어주는 거 성공, 이제 시간별로 해줘야 함.
def getDays():
    for i in range(1,7):
        for j in range(1,8):
            selector = f'#root > main > section.section_calendar > div > div.section_content > div.calendar_area > div > table > tbody > tr:nth-child({i}) > td:nth-child({j}) > button.calendar_date'
            elements = soup.select(selector)
            for element in elements:
                if 'calendar_date' in element.get('class', []) and 'unselectable' not in element.get('class', []) and 'closed' not in element.get('class',[]):
                    date = element.find('span', class_='num').text
                    dates.append(date)
    return dates


def getTimes():
    import tiki
    
    for i in range(1,7):
        for j in range(1,8):
            selector = f'#root > main > section.section_calendar > div > div.section_content > div.calendar_area > div > table > tbody > tr:nth-child({i}) > td:nth-child({j}) > button.calendar_date'
            elements = soup.select(selector)
            for element in elements:
                if 'calendar_date' in element.get('class', []) and 'unselectable' not in element.get('class', []):
                    date = element.find('span', class_='num').text
                    if date == tiki.res_day():
                        date_element = driver.find_element(By.CSS_SELECTOR, selector)
                        date_element.click()

                        for i in range(1,7):  
                            time_selector = f'#root > main > section.section_calendar > div > div.section_content > div.time_area > div > ul > li:nth-child({i}) > button.btn_time'
                            time_elements = driver.find_elements(By.CSS_SELECTOR, time_selector)
                            for time_element in time_elements:
                                if 'unselectable' not in time_element.get_attribute('class'):
                                    times.append(time_element.text)                    
    return times

def paymentF():
    #TODO
    #아이디 비밀번호 2차 받아오기
    #예약하기 버튼 클릭
    #아이디 비밀번호 입력하기
    #스크롤 쭉 내려서 결제하기
    #아이디 비밀번호 어떻게 받아올 지 생각좀 해봐. 그냥 가져오면 None값 들어가있어.
    import tiki