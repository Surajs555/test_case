import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

                                        # fixture is a special type of method
@pytest.mark.usefixtures("setup")       # fixture gets execute before and after function or class
class BaseClass:                        # fixture can be attach to any other method or class which will be executed before executing that particular method or class
                                        # it is marker but inbuilt marker.. usefixtures()
    def getLogger(self):                # All this method are public method # BaseClass,jitene be method hai just register
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)  # method -test pass

# Select class use -dropdown related operation performance(make select object)
# Locator - Requirement Constructor loctor and  element pass
##DOM => Document object model
## Visibility =>  element is avaible in HTML and visible on web page
## presence =>  element is available on HTML page ## may be or may not be visible on web page