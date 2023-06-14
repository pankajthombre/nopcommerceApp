#nopcommerce Application login test page

from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login  #import "login" class
from utilities.readPropertise import Readconfig #import Readconfig class
from utilities.customerLogger import LogGen #import Loggen class


class Test_001_Login:
    baseurl = Readconfig.getApplicationURL() #called method from readproperties module
    username = Readconfig.getUsermail() #called method from readproperties module
    password = Readconfig.getPassword() #called method from readproperties module
    logger = LogGen.loggen() #called loggen method from LogGen class

    @pytest.mark.regrssion                      #added marker to run group of test cases
    def test_homepagetitle(self,setup):
        self.logger.info("********************Test_001_Login*****************")
        self.logger.info("************Verify Home PAge Title*****************")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************Home Page title test is passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png") #captured Screenshot
            self.driver.close()
            assert False
            self.logger.info("*************Home Page title test is failed**************")

    @pytest.mark.sanity                   #added marker to run group of test cases
    @pytest.mark.regrssion
    def test_login(self,setup):
        self.logger.info("Verify Login Page")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)  #created Login class object to access methods
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.Password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopcommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*****************Login Test is passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png") #captured Screenshot
            self.driver.close()
            assert False
            self.logger.info("*****************Login Test is failed*************")






