import unittest
from selenium import webdriver
import time
import warnings
import urllib3

from time import sleep
from PageObject.Pages.LoginPage import Login
from PageObject.Pages.ProductPage import Product 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window() 
 
    def tearDown(self):
        try:
            ProductPage = Product(self.driver)
            ProductPage.getdropdown().click()
            dropdown_filter = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select')))
            logout = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]')))
            print("Logging off")
            logout.click()  
            time.sleep(2)
        except:
            print("No need to logout from page")
        finally:
            if (self.driver != None):
                print("Cleanup of test environment")
                self.driver.close()
                self.driver.quit()