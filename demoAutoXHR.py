import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def demo_run():
    for i in range(10):
        driver = webdriver.Chrome()
        # call selenium driver
        # driver = webdriver.Chrome('chromedriver.exe')
        # get함수는 해당 웹사이트를 띄워준다.
        driver.get("http://heart.stclab.com:5002/")        
        
        # driver.execute_script('window.open("http://heart.stclab.com:5002/");')
        time.sleep(3)
        print("웹사이트 호출 성공")
        #driver.switch_to_window(driver.window_handles[-1])
        #demo button 요소를 button1 변수에 저장
        button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
        button1.click()
        print("버튼 클릭성공")
        print(i+1,"번째 수행완료")

if __name__ == '__main__':
    demo_run()
