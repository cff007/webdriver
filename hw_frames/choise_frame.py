#coding=utf-8
from selenium import webdriver
from time import sleep
import os
import random

file_path = 'file:///'+os.path.abspath('frame.html')

dr = webdriver.Chrome()
dr.get(file_path)

#打印出当前页面的frame数
frames = dr.find_elements_by_tag_name('iframe')
print 'There are %s frames in this page.' %len(frames)
sleep(3)

#随机选中一个frame
num = random.randint(0,len(frames)-1)
frame = frames[num]

#switch to frame
dr.switch_to_frame(frame)
sleep(5)

#以下代码用于验证是否切换到frame
dr.find_element_by_tag_name('button').click()
sleep(3)

try:
	alert = dr.switch_to_alert()
	print alert.text
	alert.accept()
except:
	print 'no alerts display'


dr.quit()