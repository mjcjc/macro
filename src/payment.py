from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# TODO
#여기서는 결제 하는 과정을 해야함.
#
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options) # 크롬 드라이버의 경로를 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

#일준 
url = "https://booking.naver.com/booking/13/bizes/780595/items/5428141?theme=place&area=ple"
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
driver.get(url)


time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

dates = []



driver.quit()


