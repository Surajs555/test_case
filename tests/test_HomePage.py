
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData  ## impoting classes from our projet folders   # jetne be functinality hai ham use krna hai execute krna hai
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):      ## inheritance (OOP conspect use)
    '''
        TestHomePage => Child class
        BaseClass => Parent class
        inheritance # we are inheriting BaseClass into TestHomePage
        So all the properties of base class will be available to child
        All properties or methods will be inherited in child
    '''

    # Actual mai hoga test_formSubmission execute start krga  ## All properties include # valid test case
    def test_formSubmission(self,getData):    # self means object# konsa wala-which is been used by parent BaseClass # getdata -test function parameter pass # fixture pass(execute)1ke method ander se 2re method pass krne hai to fixture
        log = self.getLogger()      ## creating logger object to maintain or write logs
        ## self.driver we will get from setup fixture which is been used by parent BaseClass
        homepage= HomePage(self.driver)     ## Creating object of HomePage and passing driver in parameterized contructor
        log.info("first name is "+getData["firstname"])  # any info write
        homepage.getName().send_keys(getData["firstname"]) # homepage-object # getName()-make public method,jo kykrti hai return, web element by finding name #put into textbox (send_keys ku krna hai osa text box ke ander kuch input dalana hai)
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()      # Radio button
        self.selectOptionByText(homepage.getGender(), getData["gender"])   # selectOptionByText-method ander two pass method 1to elememt-homepage.getGender(),

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[{"firstname": "Sagar", "lastname":"Sarade", "gender": "Male"}, {"firstname": "Yusuf", "lastname": "Tamboli", "gender": "Male"}])  # one list pass in two dictionary use
    ###@pytest.fixture(params=HomePageData.getTestData("Testcase2")) #fixture ander two parameterized pass :- 1 staic(hardcoded) 2.dymaical
    def getData(self, request):      #request is default object of fixture which automatically initilized when fixture is being executed
        return request.param
#request is inbuilt object
#params - ander multiple elements
#param - only single elements
#Populate means put in value

