from selenium import webdriver
import pytest

#created below fixture to run TC on chrome or firefox browser

# To run test on desired browser:
# -	Pytest -s -v testcases/test_login.py –browser chrome
# -	Pytest -s -v testcases/test_login.py –browser firefox

@pytest.fixture()
def setup(browser):
    if  browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching chrome browser")
    # driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriverlatest\chromedriver.exe")
    elif
        browser=="firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_adoption(parser): #this will get the value from CLI/hooks
    parser.addoption("--browser")

def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")

#********************HTML Report************************************

#it is hook for adding environment info to HTML Report
def pytest_Configre(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester Name'] = 'Pankaj'

#it is hook for deleting/modify environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home",None)
    metadata.pop("Plugins", None)

