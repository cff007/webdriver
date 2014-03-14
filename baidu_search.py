#coding=utf-8
#baidu_search

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
url = "http://www.baidu.com"
dr.get(url)
sleep(5)

kw = dr.find_element_by_id('kw')
kw.send_keys('selenium')
sleep(3)

search = dr.find_element_by_id('su')
search.click()
sleep(5)

print "Title of current page is %s." %(dr.title)
print "Url of current page is %s." %(dr.current_url)

dr.quit()
