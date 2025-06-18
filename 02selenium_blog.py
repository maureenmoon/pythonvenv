from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
# from random import random
from random import uniform
import os
from dotenv import load_dotenv # env 비번 노출방지를 위해
import pyperclip

load_dotenv()

def r_sleep(min_sec=2, max_sec=5):
    wait_time = uniform(min_sec,max_sec)
    print(f'{wait_time:.2f} second waiting')
    time.sleep(wait_time)

options = webdriver.ChromeOptions() #웹 브라우저 창 키우기
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://nid.naver.com/nidlogin.login') #page change

# time.sleep(10)

# print(random()) # 0 ~1 사이값
# print(uniform(2,5))
time.sleep(uniform(2,5)) #사람인 척 하여 접근거절당하는 경우를 없앰

NAVER_ID = os.getenv("NAVER_ID")
NAVER_PW = os.getenv("NAVER_PW")
# print(NAVER_ID)

# input id
id_input = driver.find_element(By.ID, 'id') # ID= class name #''안의 정보는  source에 없는 데이터를 넣고 실행하면 바로 중단된다
pyperclip.copy(NAVER_ID)
id_input.click()
id_input.send_keys(Keys.CONTROL,'v')
# time.sleep(uniform(2,5))
r_sleep()

# input pw
pw_input = driver.find_element(By.ID, 'pw') 
pyperclip.copy(NAVER_PW)
pw_input.click()
pw_input.send_keys(Keys.CONTROL,'v')

login_input = driver.find_element(By.ID, 'log.login') 
login_input.click()
# time.sleep(uniform(2,5))
r_sleep()

# page moving
driver.get('https://blog.naver.com/GoBlogWrite.naver') #page change
# time.sleep(uniform(2,5))
r_sleep()

#ifram in
iframe = driver.find_element(By.ID,'mainFrame')
driver.switch_to.frame(iframe)
r_sleep()

try:
    pop_cancle_btn = driver.find_element(By.CLASS_NAME,'se-popup-button-cancle')
    pop_cancle_btn.click()
    print('you have a pop-up')
    r_sleep()
except:
    print('no pop-up')

try:
    help_cancle_btn = driver.find_element(By.CLASS_NAME,'se-help-panel-close-button')
    help_cancle_btn.click()
    print('you have help')
    r_sleep()
except:
    print('no help')

#input data
title_text = "안녕하세요, 여행을 사랑하는 모든 분들께!"
body_text = (
    "설레는 발걸음으로 시작되는 여행의 순간들, 낯선 거리에서 마주치는 예상치 못한 만남들, "
    "그리고 새로운 문화와 풍경 속에서 느끼는 감동을 이 공간에 담아보려 합니다. "
    "여행은 단순한 이동이 아닌, 나를 발견하고 세상을 더 넓게 바라보는 소중한 시간이라고 생각합니다.\n"
    "앞으로 제가 경험한 특별한 순간들과 여행 팁을 여러분과 나누며, 함께 성장하는 여행 커뮤니티를 만들어가길 희망합니다. "
    "여러분의 발자국도 이 여정에 함께해주세요!"
)

TYPE_DELAY = 0.1

try:
    title_input = driver.find_element(By.CSS_SELECTOR,'div.se-section-documentTitle')
    # pyperclip.copy(title_text)
    # print(title_text)
    title_input.click()

    # title_input.send_keys(Keys.CONTROL,'v')
    # title_input.send_keys(title_text)
    actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() #아래 방법이 입력 시간조정이 가능하여 더 좋은 방법임

    #입력을 사람처럼 한자한자 넣게 함
    for char in title_text:
        actions.send_keys(char).perform()
        time.sleep(TYPE_DELAY)

    r_sleep()
except:
    print('no paragraph')

try:
    content_input = driver.find_element(By.CSS_SELECTOR,'div.se-section-text')
    # pyperclip.copy(title_text)
    # print(title_text)
    content_input.click()

    # title_input.send_keys(Keys.CONTROL,'v')
    # title_input.send_keys(title_text)
    actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() #아래 방법이 입력 시간조정이 가능하여 더 좋은 방법임

    #입력을 사람처럼 한자한자 넣게 함
    for char in body_text:
        actions.send_keys('\n' if char == '\n' else char).perform() #줄바꿈 확인기능 추가
        time.sleep(TYPE_DELAY)

    r_sleep()
except:
    print('no body')

save_button = driver.find_element(By.CLASS_NAME,'save_btn__bzc5B')
save_button.click()
print('write completed')
r_sleep()

input('input data') # cmd에서 입력하면 창이 닫힘