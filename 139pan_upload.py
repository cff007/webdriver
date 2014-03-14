#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time

dr = webdriver.Chrome()
url = 'http://mail.10086.cn/'
dr.get(url)
dr.implicitly_wait(10)

#登录
dr.find_element_by_id('txtUserName').send_keys('15219489893')
dr.find_element_by_name('Password').send_keys('chenfang8187')
dr.find_element_by_id('loginBtn').click()
time.sleep(10)

#切换到新版，进入139网盘模块
dr.find_element_by_id('gotoMatrix2').click()
time.sleep(5)
dr.find_element_by_css_selector('i[class=i_netDisk]').click()
time.sleep(5)

#定位到上传按钮所在的frame
dr.switch_to_frame('diskDev')
time.sleep(5)

#上传文件
dr.find_element_by_name('uploadInput').send_keys('C:\Python27\chromedriver.exe')
time.sleep(10)

dr.quit()