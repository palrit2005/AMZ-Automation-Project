# AMZ-Automation-Project

This Project is to automate the searching of least cost Item ("Selenium Books") on the amazon site.
I have used Selenium framework using Python language. 
In the project I have made 2 PyDev packages- testcases and testresources and config.properties file and conftest module.
testcases package contains test_login4 module, where Iam running my testcase.
testresources package contains applicationkeywords1, generickeywords1 and validatekeywords1 modules.
In generickeywords1 module I have created functions for implementing the functionality. It also has inherited the functionality of applicationkeywords1 and validatekeywords1 module.
  openBrowser function is used to open the browser of your choice. I have choosen mozilla as my browser.
  navigate function is used to open the url-  www.amazon.com
  click function is used to implement the button click functionality.
  type function is used to automate the typing of text- Selenium books.
  getNextButtonByCSS function is used to click on Next button present at the buttom to move to next page.
  getElementsList fuction is to get the list of books present in the page.
  Then I have created few common utility fuctions which are being used inside the other fuctions- isElementPresent, getElement, Quit.
validatekeywords1 module is used basically for the allure reports, logs.
  In this module, I have made the fuctions- takeScreenshot, logging, reportFailure, reportSuccess to see the final output.
config.properties contains the url, xpaths, css path for the elements present in the application.
In conftest module, I have define the fixture to setup and teardown the resources.

 Allure Report link- http://192.168.1.8:60443/index.html#suites/b45bcae7d7cb42293b7e32089150789b/95ff3fecf0f42f25/
 

