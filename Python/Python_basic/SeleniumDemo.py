import unittest
from selenium import webdriver
from time import sleep
import datetime

class MyfirstTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Users\SARFRAZ ANSARI\Desktop\Automation\Selenium\Selenium_Webdrivers\geckodriver.exe")

    def test_demo(self):
        driver=self.driver
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_linkText("image").click()
        self.driver.navigate().refresh()
        self.driver.navigate().back()
        self.sleep(5)

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
