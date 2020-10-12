'''
Created on 11-Oct-2020

@author: palri
'''
import logging
import allure
from _datetime import datetime 
from allure_commons.types import AttachmentType
    
class validatekeywords:
    
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.ERROR)
        
    def takeScreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),"Screenshot at :"+str(datetime.now()),AttachmentType.PNG)
    
    def logging(self,message):
        self.logger.info(message)
    
    def reportFailure(self,message):
        self.takeScreenshot()
        assert False, message
    
    def reportSuccess(self,message):
        assert True, message
        
        