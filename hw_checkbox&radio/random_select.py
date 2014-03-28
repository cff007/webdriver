#coding=utf-8
from selenium import webdriver
from time import sleep
import os
import random

file_path='file:///'+os.path.abspath('checkbox&radio.html')

dr = webdriver.Chrome()
dr.get(file_path)
sleep(4)

#获得当前页面的radio总数
rds = dr.find_elements_by_name('fruit')
a = len(rds)

#获得当前页面的checkbox总数
cbs = dr.find_elements_by_name('colour')
b = len(cbs)

def random_select(what,count):
	if (what==rds and count>1):
		print "You can only select one radio. "
	elif (what==cbs and count>b):
		print "Checkboxes you select can't go over the exist. "
	else:
		for i in range(0,count):
			el = random.choice(what)
			el.click()
			what.remove(el)  #这条语句用来从what列表中删除已选中的元素，防止重复选择
			sleep(2)

random_select(rds,1)
random_select(rds,2)
random_select(cbs,3)
random_select(cbs,6)
random_select(cbs,0)
sleep(5)

dr.quit()

