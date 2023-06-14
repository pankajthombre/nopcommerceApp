#nopcommerce Application login test page
import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login  #import "login" class
from utilities.readPropertise import Readconfig #import Readconfig class
from utilities.customerLogger import LogGen #import Loggen class
from utilities import XLUtils #import XLUtils class

#test_login Page by Data driven --> taking data from excel sheet
class Test_002_DDT_Login:
    baseurl = Readconfig.getApplicationURL() #called method from readproperties module
    path=".//TestData/LoginData.xlsx" #path of test data excel file
    logger = LogGen.loggen() #called loggen method from LogGen class

    def test_login_ddt(self,setup):
        self.logger.info("****************Test_002_DDT_Login********************")
        self.logger.info("****************Verifying Login DDT Test********************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)  #created Login class object to access methods

        XLUtils.getRowcount(self.path,"Sheet1")
        print("number of rows i in excel",self.rows)

        lst_status=[] #empty list status
        for r in range(2,self.rows+1):
            self.user=XLUtils.readdata(self.path,'Sheet1',r,1)
            self.password=XLUtils.readdata(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readdata(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.Password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title= "Dashboard / nopcommerce administration"
            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Passed")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***Failed")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                     if self.exp == "Pass":
                        self.logger.info("***Failed")
                        lst_status.append("Pass")
                     elif self.exp == "Fail":
                        self.logger.info("***Failed")
                        lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("******Login DDT test Passed*****")
                self.driver.close()
                assert True
            else:
                self.logger.info("***********Login DDT test Failed*****")
                self.driver.close()
                assert False

            self.logger.info("******end of login DDT Test")
            self.logger.info("********completed TC_002_LoginDDT**********")








