from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
import unittest
from Selenium_Python import LoginPage
from Selenium_Python import HomePage

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome("C:\Selenium_Webdrivers\chromedriver.exe") # Place you Selenium Webdriver loacation here!!!
        print("*****************************************************************")
        print("Test started at " + str(datetime.datetime.now()))


    def test_hrm(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        driver.implicityl_wait(10)

# Page Object model for the LoginPage
        login=LoginPage(driver)
        login.enter_userName("Admin")
        login.enter_password("admin123")
        login.click_login()

# Page object model for the Dashboard and Logout page.
        home=HomePage(driver)
        home.click_Welcome()
        home.click_Logout()



    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test finished at at " + str(datetime.datetime.now()))
        print("*****************************************************************")


if __name__ == '__main__':
    unittest.main()
