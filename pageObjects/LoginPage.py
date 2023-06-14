#nopcommerce Application login page

class Login:
    #Locators of login page
    textbox_username_id="Email"  #username textbox
    testbox_password_id="Password"      #password textbox
    login_button_xapth="//button[normalize-space()='Log in']"  #login button
    logout_link_linktest="Logout" #logout option

    #constructor defined
    def __init__(self,driver): #capture the driver from testcases,and that driver initating to class variable
        self.driver=driver #this driver used to call class locators

    def setUserName(self,username): # find username webelement and pass parameter to method
        self.find_element_by_id(self.textbox_username_id).clear()
        self.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password): # find password webelement and pass parameter to method
        self.find_element_by_id(self.testbox_password_id).clear()
        self.find_element_by_id(self.testbox_password_id).send_keys(password)

    def clicklogin(self): #find login button and perform click action
        self.find_element_by_xpath(self.login_button_xapth).click()

    def clicklogout(self): #find logout option and perform click action
        self.find_element_by_xpath(self.logout_link_linktest).click()





