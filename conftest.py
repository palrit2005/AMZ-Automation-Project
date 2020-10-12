'''
Created on 11-Oct-2020

@author: palri
'''
from pyjavaproperties import Properties
import pytest
import allure
from testresources.generickeywords7 import generickeywords

prop = Properties()

@pytest.yield_fixture(scope='session',autouse=True)
def base_fixture():
    with allure.step(" Initiallizing properties file...."):
        propertiesFile = open("C:\\Users\\palri\\eclipse-workspace\\AmazonProject\\config.properties")
        prop.load(propertiesFile)
        prop.list()
        gen=generickeywords()
        
    yield locals()
    with allure.step("Quitting as tear down process....."):
        try:
            gen.Quit()
        except Exception as e:
            print(e)
