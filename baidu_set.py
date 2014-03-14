#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time

dr = webdriver.Chrome()
url = 'http://www.baidu.com/'
dr.get(url)
dr.implicitly_wait(10)

#找到搜索设置
dr.find_element_by_link_text('搜索设置').click()
WebDriverWait(dr,10).until(lambda dr:dr.find_element_by_id('nr').is_displayed())

#定位到“每页显示50条”
dr.find_element_by_id('nr').find_elements_by_tag_name('option')[2].click()

#保存设置
buttons = dr.find_elements_by_css_selector('input[type=button]')
for button in buttons:
	if button.get_attribute('onclick') == 'go()':
		button.click()
		break
#buttons[1].click()
time.sleep(5)

try:
	alert = dr.switch_to_alert()
	#print alert.text
	alert.accept()
except:
	"Error"

time.sleep(5)

dr.quit()