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

#URL info
path = ".\chromedriver.exe"
loginurl = "https://onprem-dev.stclab.com/en/on_prem/signin"
basic = "https://qa-console.surffy-dev.io/ko/byol/console/product/nf/65/controls/basic/default"

#seg URL
# segURL = "http://heart.stclab.com:5002/"
segURL = "https://image.surffy.io/demo/json/learn_2.json/"

#진입
driver = webdriver.Chrome(path)
driver.get(loginurl)

#sleep 시간
sec = 1

#세그먼트 반복 수
segCount = 10

#login info
consoleid = 'kade01'
password = 'qwe123!!'

#로그인
driver.find_element(By.NAME, 'id').send_keys(consoleid)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'css-19rzuai').click()
time.sleep(sec)

#콘솔 홈
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[3]/div[1]/button').click()
time.sleep(sec)

# 첫번째 프로젝트
# driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div[2]/div/div/ul[1]').click()
# 두번째 프로젝트
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div[2]/div/div/ul[2]').click()
time.sleep(sec)

#기본제어 진입
# driver.find_element(By.XPATH, '').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[1]/div[2]/div[2]/div[2]').click()
time.sleep(sec)

#기본제어 모달 생성 반복문
for num in range(segCount):
    # 세그먼트 명을 string 으로 반환
    segnameArr = ["testxhr", num]
    segname = ''.join(str(s) for s in segnameArr)
    # URL을 string 으로 반환
    segurlArr = [segURL, num]
    segurlname = ''.join(str(s) for s in segurlArr)
    #모달저장
    driver.find_element(By.CLASS_NAME, 'css-phyh84').click()
    time.sleep(sec)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[2]/div[1]/div[2]/input').send_keys(segname)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[2]/div[3]/div[2]/input').send_keys(segurlname)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[2]/div[8]/div[2]/input').send_keys(num)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[3]/button').click()
    time.sleep(sec)
time.sleep(1000)
driver.close