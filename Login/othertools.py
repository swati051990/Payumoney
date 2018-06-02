'''
Created on May 29, 2018

@author: HP
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.payumoney.com/")
driver.maximize_window() 
driver.find_element_by_xpath("//a[@href='#/otherTools']").click()
