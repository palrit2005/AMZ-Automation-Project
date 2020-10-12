'''
Created on 11-Oct-2020

@author: palri
'''
from selenium import webdriver
import time
import conftest


def test_login4(base_fixture):
    base_fixture['gen'].openBrowser("mozilla")
    base_fixture['gen'].navigate("URL")
    time.sleep(10)
    base_fixture['gen'].type("searchTextbox_xpath", "Selenium Testing books")
    base_fixture['gen'].click("searchButton_xpath")
    base_fixture['gen'].getNextButtonByCSS('a-last')
    time.sleep(10)
    base_fixture['gen'].getElementsList('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div')
    #base_fixture['gen'].selectProduct("selectBook_xpath").select()
    #base_fixture.find_element_by_xpath("selectBook_xpath").click()
    #base_fixture['gen'].click("signIn_xpath")
    
    #time.sleep(5)