#coding=utf-8
#baidu_login

from selenium import webdriver
import time

dr = webdriver.Chrome()
url = 'http://www.baidu.com/'
dr.get(url)

#-------------------by link--------------------------
#----------------------------------------------
login = dr.find_element_by_link_text('登录')
login.click()
time.sleep(10)
print "Current url is:%r" %(dr.current_url)

#--------------登录-----------------------
username = dr.find_element_by_name('userName')
username.send_keys('xxxxxx')
time.sleep(3)

pw = dr.find_element_by_name('password')
pw.send_keys('xxxxxx')
time.sleep(3)

login_bt = dr.find_element_by_id('TANGRAM__PSP_8__submit')
login_bt.click()
time.sleep(3)