'''
Created on May 29, 2018

@author: HP
'''
#LOGIN WITH VALID CREDIENTIALS
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.payumoney.com/")
driver.maximize_window() 
driver.find_element_by_xpath("//a[@href='/merchant-account/#/login']").click()
driver.find_element_by_name("email").send_keys("k.agarwal4@gmail.com")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(7)
driver.find_element_by_xpath("//input[@type='password']").send_keys("Walk'n'shine@1988")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(6)
driver.find_element_by_xpath("//a[@href='#/otherTools']").click()
driver.find_element_by_xpath("//a[@href='/merchant/store']").click()
#time.sleep(9)
#driver.find_element_by_xpath("//a[href='/merchant/store/add']").click()


