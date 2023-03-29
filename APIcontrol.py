import selenium.webdriver.support.ui as ui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#chromedriver 경로 설정
CHROMEDRIVER_PATH = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--start-maximized')

# 반복할 호출 수
count = 10

# 브라우저 실행 및 탭 추가
driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
for dirver in range(count):
    driver.execute_script('window.open("about:blank", "_blank");')
    tabs = driver.window_handles

# 탭 핸들링
for num in range(count):
    # TAB_num
    driver.switch_to.window(tabs[num])
    driver.get('http://heart.stclab.com:5002')
    button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/a[4]')
    button1.click()
    time.sleep(1)
    # button2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/a[5]')
    # button2.click()
    # time.sleep(2)
    print(num+1,'번째 호출 완료')


print('url 부하 테스트 완료')
time.sleep(10)
driver.quit