from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from random import random
from random import uniform
import os
from dotenv import load_dotenv
import pyperclip

load_dotenv()

def r_sleep(min_sec=2, max_sec=5):
    wait_time = uniform(min_sec,max_sec)
    print(f'{wait_time:.2f} second waiting')
    time.sleep(wait_time)

options = webdriver.ChromeOptions() #웹 브라우저 창 키우기
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://auth.band.us/login_page') #page change

# time.sleep(10)

# print(random()) # 0 ~1 사이값
# print(uniform(2,5))
time.sleep(uniform(2,5)) #사람인 척 하여 접근거절당하는 경우를 없앰

NAVER_ID = os.getenv("NAVER_ID")
NAVER_PW = os.getenv("NAVER_PW")
CellPhone = os.geteng("CellPhone")
# print(NAVER_ID)

#choose login method
# loginType = driver.find_element(By.CSS_SELECTOR, '.loginBtnList li a') # ID= class name #''안의 정보는  source에 없는 데이터를 넣고 실행하면 바로 중단된다
loginType = driver.find_element(By.CLASS_NAME, '-naver') 
loginType.click()


# input id
driver.get('https://nid.naver.com/oauth2.0/authorize') #page change

id_input = driver.find_element(By.ID, 'phone_login_a') 
pyperclip.copy(CellPhone)
id_input.click()
# id_input.send_keys(Keys.CONTROL,'v')
# time.sleep(uniform(2,5))
r_sleep()


input('input data') # cmd에서 입력하면 창이 닫힘write