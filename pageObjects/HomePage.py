from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    '''
        POM  => Page object model       #Interviw#POM -In POM we will be writing all the selector in one of the class

    '''
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    __name = (By.CSS_SELECTOR, "[name='name']")     #private attribute,encapsulation ,readonly# To Find -name
    __email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")                  #diff -XPATH can trival forward and reversed
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")   #CSS_SELECTOR can trival only forward

    # this all method
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.__name)     ##__name -Encapsulation use kiya
                                #self.name be chalega

    def getEmail(self):
        return self.driver.find_element(*HomePage.__email)    # * is used to unpack tuple in parameters
        ## HomePage.email[0], HomePage.email[1] => *HomePage.email


    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)


# All elements find
# All web control find kiya hai

