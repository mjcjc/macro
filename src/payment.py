# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # 웹 드라이버를 초기화합니다. (Chrome을 사용한다고 가정)
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options) 
# # 웹페이지를 엽니다.
# url = "https://booking.naver.com/booking/13/bizes/780595/items/5428141?theme=place&area=ple"
# driver.get(url)

# # 날짜를 선택합니다. (예: 5일 후)
# wait = WebDriverWait(driver, 15)
# calendar = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'calendar_body')))
# days = calendar.find_elements(By.CSS_SELECTOR, 'td')
# days[3].click()  # 5일 후를 선택합니다.

# # 'calendar_area'와 'time_area' 클래스를 찾습니다.
# section_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'section_content')))
# calendar_area = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'calendar_area')))
# time_area = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'time_area')))

# # 각 영역의 텍스트를 추출합니다.
# calendar_text = calendar_area.text
# time_text = time_area.text

# print("Calendar Area Text: ", calendar_text)
# print("Time Area Text: ", time_text)

# # 웹 드라이버를 종료합니다.
# driver.quit()
