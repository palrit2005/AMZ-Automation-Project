'''
Created on 11-Oct-2020

@author: palri
'''
from selenium import webdriver
from pyjavaproperties import Properties
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _overlapped import NULL
import conftest
import allure
from testresources.applicationkeywords1 import applicationKeywords
from testresources.validatekeywords1 import validatekeywords
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from lib2to3.tests.support import driver

class generickeywords(applicationKeywords,validatekeywords):
    def __init__(self):
        self.prop = conftest.prop  
        
    def openBrowser(self,browsername):
        with allure.step("Opening browser  -"+ browsername):
            if(browsername== 'mozilla'):
                path= "C:\\Users\\palri\\PycharmProjects\\Selenium\\Drivers\\geckodriver"
                self.driver= webdriver.Firefox(executable_path=path)
                print("generic "+str(self.driver))
            elif(browsername== 'chrome'):
                path= "C:\\Users\\palri\\PycharmProjects\\Selenium\\Drivers\\chromedriver"
                driver= webdriver.Chrome(executable_path=path)
            self.takeScreenshot()
        
    def navigate(self,url):
        with allure.step("Navigating on  -"+ url):
            print("generic Driver ===="+str(self.driver))
            URL = self.prop[url]
            self.driver.get(URL)
            
    def click(self,elementtobeclicked):
        with allure.step("click on  -"+ elementtobeclicked):
            self.getElement(elementtobeclicked).click()
     
    
    def type(self,element,data):
        with allure.step("Typing in -"+ element):
            self.getElement(element).send_keys(data)   
    
    
    def clickBook(self,element):
        self.lowestPrice1(element).click()
        
    def getNextButtonByCSS(self,element_to_be_selected):
        self.driver.find_element_by_css_selector('.'+str(element_to_be_selected)).click()
            
    def getElementsList(self,element_to_be_selected):
        ax= self.driver.find_elements_by_xpath(element_to_be_selected)
        print(len(ax))
        for element in ax:
            for sElement in element.find_elements_by_tag_name('span.a-price'):
                #print('priceX '+str(sElement.text.encode('utf-8')))
                print('innerV  '+ str(sElement.find_elements_by_tag_name('span.a-offscreen')))
                for inElement in sElement.find_elements_by_tag_name('span.a-offscreen'):
                    print('price '+str(inElement.text.encode('utf-8')))
                    print(inElement.find_element_by_xpath("./../.."))
            
            print("=============================================")
            
                
    #common utility function
            
    def isElementPresent(self,locatorkey):
        wait = WebDriverWait(self.driver,20)
        elementList = []
        obj = self.prop[locatorkey]
        if(locatorkey.endswith("_xpath")):
            elementList = wait.until(EC.presence_of_all_elements_located((By.XPATH,obj)))
        elif(locatorkey.endswith("_id")):
            elementList = wait.until(EC.presence_of_all_elements_located((By.ID,obj)))
        elif(locatorkey.endswith("_name")):
            elementList = wait.until(EC.presence_of_all_elements_located((By.NAME,obj))) 
            
        if(len(elementList)==0):
            return False
        else:
            return True
        
    def getElement(self,locatorKey):
        obj = self.prop[locatorKey]
        element = NULL
        if(self.isElementPresent(locatorKey)):
            try:
                if(locatorKey.endswith("_xpath")):
                    element = self.driver.find_element('xpath', obj)
                elif(locatorKey.endswith("_id")):
                    element = self.driver.find_element('id', obj)
                elif(locatorKey.endswith("_name")):
                    element = self.driver.find_element('name', obj)
                return element
            except Exception:
                print("element not found")
        else:
            print("Element not present "+locatorKey)      
            
    def lowestPrice(self):
        list1 = []
        num = int(input("Cost of books in list: ")) 
        for i in range(1, num + 1): 
            ele= int(input("Enter cost: ")) 
            list1.append(ele) 
        print("Smallest cost is:", min(list1))
        
        
    def lowestPrice1(self,element):
        list1 = []
        num = int(input("Cost of books in list: ")) 
        for i in range(0, num + 1): 
            ele= int(input("Enter cost: ")) 
            list1.append(ele) 
        print("Smallest cost is:", min(list1))
        self.driver.findElement(element).click()
        
        
                
    def Quit(self):
        if(self.driver!=NULL):
            self.driver.quit()
        else:
            print("No driver to close")   