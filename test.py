from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# driver.get("http://heart.stclab.com:5002/")
# time.sleep(3)
# for i in range (5):
driver.execute_script('window.open("http://heart.stclab.com:5002/");')
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])  
print("성공?")
button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
print("실패?")


driver.execute_script('window.open("http://heart.stclab.com:5002/");')
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])  
print("성공??")

button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
print("실패?")


# driver.close()

print(driver.window_handles)