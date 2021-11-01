import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class Checkout(object):
    def __init__(self, driver):
        self.driver = driver
        self.checkoutlogo = driver.find_element(By.XPATH, Locator.checkoutlogo)
        self.infoname = driver.find_element(By.XPATH, Locator.infoname)
        self.infolastname = driver.find_element(By.XPATH, Locator.infolastname)
        self.infozip = driver.find_element(By.XPATH, Locator.infozip)
        self.confirmshop = driver.find_element(By.XPATH, Locator.confirmshop)

    def getcheckoutlogo(self):
        return self.checkoutlogo

    def getinfoname(self):
        return self.infoname

    def getinfolastname(self):
        return self.infolastname

    def getinfozip(self):
        return self.infozip

    def getconfirmshop(self):
        return self.confirmshop