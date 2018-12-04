from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  Select
from time import  sleep
import datetime

import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Users\SARFRAZ ANSARI\Desktop\Ride\chromedriver.exe")
        print("========================================")
        print("environment Created at: " + str(datetime.datetime.now()))

    def test_fb(self):
        self.driver.get("https://www.facebook.com")
        Select(self.driver.find_element_by_id('day')).select_by_index('2')
        Select(self.driver.find_element_by_id('month')).select_by_index('3')
        Select(self.driver.find_element_by_id('year')).select_by_index('3')
        self.driver.navigate().to("https://google.com.sa")


    def tearDown(self):
        print("environment destroyed at: " + str(datetime.datetime.now()))
        print("========================================")


if __name__ == '__main__':
    unittest.main()
