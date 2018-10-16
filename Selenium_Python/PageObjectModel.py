from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import datetime
import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome("C:\Selenium_Webdrivers\chromedriver.exe") # Place you Selenium Webdriver loacation here!!!
        print("*****************************************************************")
        print("Test started at " + str(datetime.timedelta.now()))


    def test_hrm(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.maximize_window()
        self.driver.implicityl_wait(10)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

        sleep(10)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("logout").click()



      #Remaining test Keysqord will come here and you can extend this  according the complexity of your testcases

        #your code will be here .......





    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test finished at at " + str(datetime.datetime.now()))
        print("*****************************************************************")


if __name__ == '__main__':
    unittest.main()
