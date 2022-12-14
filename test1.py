from threading import Thread
import queue
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locator = (By.ID, 'ht-login')
input_email = (By.ID, '_email')
input_pwd = (By.ID, '_password')
commit_button = (By.XPATH, '//button[@type="button" and  @tabindex="4"]')

users = [{"email": "shiyong@tetx.com", "pwd": "1234567"}, {"email": "ys@tetx.com", "pwd": "123456"}]

que = queue.Queue()
for i in users:
    que.put(i)


def login(dr, que):
    data = que.get(timeout=0.01)
    dr.maximize_window()
    dr.get('https://www.azazie.com/')
    WebDriverWait(dr, 5).until(EC.visibility_of_element_located(locator))
    dr.find_element(*locator).click()
    dr.find_element(*locator).click()
    WebDriverWait(dr, 5).until(EC.visibility_of_element_located(input_email))
    dr.find_element(*input_email).send_keys(data['email'])
    dr.find_element(*input_pwd).send_keys(data['pwd'])
    time.sleep(5)
    dr.find_element(*commit_button).click()


thread_obj = []
dr_obj = []
#
# for i in range(2):
for i in range(2):
    dr = webdriver.Chrome()
    dr_obj.append(dr)
# dr = webdriver.Chrome()
# dr2 = webdriver.Chrome()
# dr_obj.append(dr)
# dr_obj.append(dr2)
for i in dr_obj:
    thread_obj.append(Thread(target=login, args=(i, que)))

for i in thread_obj:
    i.start()

for i in thread_obj:
    i.join()

print(666666666)
