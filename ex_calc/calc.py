# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import os

file_path = 'file:///' + os.path.abspath('calculator.html')

dr = webdriver.Chrome()

dr.get(file_path)

dr.maximize_window()

v1 = dr.find_element_by_id('var1')


#op_element = dr.find_element_by_id('operator')
#op = Select(op_element)

v2 = dr.find_element_by_id('var2')


eql = dr.find_element_by_id('eql')

v1.send_keys('2')
v2.send_keys('3')

eql.click()

result_element = dr.find_element_by_id('result')
result = result_element.get_attribute('value')
print result

assert result == '5'

sleep(3)

dr.quit()