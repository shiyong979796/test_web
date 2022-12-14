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
sign_out = (By.XPATH, '//*[@id="header-nav"]/div/div/div[3]/ul/li[2]/ul[1]')

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('https://www.azazie.com/')
# js="window.open('url')"
# dr.execute_script(js)
time.sleep(2)
cookies = dr.get_cookies()
print('cookies:', cookies)
WebDriverWait(dr, 5).until(EC.visibility_of_element_located(locator))
dr.find_element(*locator).click()
dr.find_element(*locator).click()
WebDriverWait(dr, 5).until(EC.visibility_of_element_located(input_email))
dr.find_element(*input_email).send_keys('shiyong@tetx.com')
dr.find_element(*input_pwd).send_keys('1234567')
dr.find_element(*commit_button).click()
time.sleep(3)

action = ActionChains(dr)

action.move_to_element(dr.find_element(*locator)).perform()
# WebDriverWait(dr, 5).until(EC.visibility_of_element_located(sign_out))
dr.find_element(*sign_out).click()
cookies = dr.get_cookie('login_token')['value']
print('这是登陆cookie：', cookies)
