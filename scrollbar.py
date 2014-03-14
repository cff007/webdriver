#coding=utf-8

from selenium import webdriver
from time import sleep
import os

file_path = 'file:///'+os.path.abspath('scrollbar.html')

dr = webdriver.Chrome()
dr.get(file_path)
sleep(5)

def scrollbar():
	alert = dr.switch_to_alert()
	sleep(5)
	if alert.text == 'Please view top news terms !':
		alert.accept()
		sleep(5)
		js = "var q=document.getElementById('text').scrollTop=10000"
		dr.execute_script(js)
		sleep(5)
		return 0
	else:
		print alert.text
		alert.accept()
		sleep(5)
		return 1

dr.find_element_by_id('submit').click()
scrollbar()
dr.find_element_by_id('submit').click()
scrollbar()

dr.quit()
