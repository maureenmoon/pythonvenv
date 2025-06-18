from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.get('https://mail.naver.com/write') #page change
# time.sleep(uniform(2,5))
r_sleep()

def read_mail_content():
    with open('mailtext.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    to_email = lines[0].split(':')[1]
    to_title = lines[1].split(':')[1]
    to_body = lines[2].split(':')[1]

    return to_email, to_title, to_body

to_mail,to_title,to_body = read_mail_content()

mail_email = driver.find_element(By.ID, 'recipient_input_element')
pyperclip.copy(to_mail)
mail_email.click()
mail_email.send_keys(Keys.CONTROL,'v')
r_sleep()

mail_title = driver.find_element(By.ID, 'subject_title')
pyperclip.copy(to_title)
mail_title.click()
mail_title.send_keys(Keys.CONTROL,'v')
r_sleep()

#iframe() 들어가기 
iframe = driver.find_element(By.CSS_SELECTOR,'.editor_body iframe') # .editor_body 밑의 iframe
driver.switch_to.frame(iframe)

mail_body = driver.find_element(By.CLASS_NAME,'workseditor-content')
pyperclip.copy(to_body)
mail_body.click()
mail_body.send_keys(Keys.CONTROL, 'v')
r_sleep()

#iframe에서 나가기
driver.switch_to.default_content() 

#send btn click
send_btb = driver.find_element(By.CLASS_NAME,'button_write_task')
send_btb.click()
r_sleep()

# input('input data') # cmd에서 입력하면 창이 닫힘