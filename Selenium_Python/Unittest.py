from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

import unittest




class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("******************************************************")
        print("******************************************************")
        self.driver = webdriver.Chrome("C:\Selenium_Webdrivers\chromedriver.exe")
        self.driver.get("http://www.facebook.com ")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()




    def test_something(self):
        driver=self.driver
        driver.get_title()
        email=driver.find_element_by_id('email').clear()
        email.send_keys("7523882655")

        passw =driver.find_element_by_id('pass').clear()
        passw.send_keys("Sarfraz@786")
        driver.get_screenshot_as_file("C:\Selenium_Webdrivers")


        driver = self.driver
        driver.find_element_by_link_text("log In")










    def tearDown(self):
        self.driver.quit()
        print("******************************************************")
        print("******************************************************")






if __name__ == '__main__':
    unittest.main()
