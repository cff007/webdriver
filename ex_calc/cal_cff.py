#coding=utf-8
#cal.py

from selenium import webdriver
import os
from selenium.webdriver.support.select import Select
from time import sleep

filepath = 'file:///'+os.path.abspath('calculator.html')
print "I'm going to open %s." %filepath

dr = webdriver.Firefox()
dr.get(filepath)
sleep(3)

var1_el = dr.find_element_by_id('var1')     #找到第1个输入框元素
var2_el = dr.find_element_by_id('var2')     #找到第2个输入框元素
eql = dr.find_element_by_id('eql')			#找到等号元素
re_el = dr.find_element_by_id('result')		#找到计算结果元素
oper_el = dr.find_element_by_id('operator') #找到运算符选择按钮元素
op = Select(oper_el)

var1_el.send_keys('2')
var2_el.send_keys('4')

# 加法运算
op.select_by_value('+')
eql.click()
result = re_el.get_attribute('value')
print result
assert result == '6'
sleep(5)

#减法运算
op.select_by_value('-')
eql.click()
result = re_el.get_attribute('value')
print result
assert result == '-2'
sleep(5)

#乘法运算
op.select_by_value('*')
eql.click()
result = re_el.get_attribute('value')
print result
assert result == '8'
sleep(5)

#除法运算
op.select_by_value('/')
eql.click()
result = re_el.get_attribute('value')
print result
assert result == '0.5'
sleep(5)

#求余
op.select_by_value('%')
eql.click()
result = re_el.get_attribute('value')
print result
assert result == '2'
sleep(5)





