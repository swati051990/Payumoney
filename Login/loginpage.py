'''
Created on May 29, 2018

@author: HP
'''
from selenium import webdriver
import os;
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.payumoney.com/")
driver.maximize_window() 

def login_with_valid_credientials():

  driver.find_element_by_xpath("//a[@href='/merchant-account/#/login']").click()
  driver.find_element_by_name("email").send_keys("k.agarwal4@gmail.com")
  driver.find_element_by_xpath("//button[@type='submit']").click()
  time.sleep(7)
  driver.find_element_by_xpath("//input[@type='password']").send_keys("Walk'n'shine@1988")
  driver.find_element_by_xpath("//button[@type='submit']").click()
  time.sleep(6)
  return True
login_with_valid_credientials()

def create_new_store():
  driver.find_element_by_xpath("//a[@href='#/otherTools']").click()
  driver.find_element_by_xpath("//a[@href='/merchant/store']").click()
  wind=driver.window_handles[2]
  driver.switch_to_window(wind)
  driver.implicitly_wait(5)
  driver.find_element_by_partial_link_text("Add Store").click()
  return True
create_new_store()

def add_details_to_createstore():
    driver.find_element_by_id("store-name-0").send_keys("APPSHOTS")
    driver.find_element_by_id("store-title-0").send_keys("Summary of new technologies")
    print os.getcwd()
    #driver.find_elements_by_link_text("/auth/op/file/download?path=logo%2F2018%2F06%2F17%2Fprod%2F20fb1b91-cd95-4219-a1dc-cf8b00038bc8_1.jpg&fileType=image/jpeg&isAttachment=0&isLogo=1").click()
    driver.find_elements_by_xpath("//input[@type='file']")[0].send_keys("C:/Python27/Workspace/Payumoney/Login/1.jpg")
    driver.find_elements_by_xpath("//input[@type='file']")[1].send_keys("C:/Python27/Workspace/Payumoney/Login/selfie-shots.jpg")
    driver.find_element_by_name("store-description-0").send_keys("find details of new technologies in short")
    driver.find_element_by_xpath("//button[@class='nw_blue_btn right bttn-create-store']").click()
    return True
add_details_to_createstore()


#print 1
#import pdb;pdb.set_trace()
