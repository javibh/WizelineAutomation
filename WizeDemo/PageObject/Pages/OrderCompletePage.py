import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class CompleteOrder(object):
    def __init__(self, driver):
        self.driver = driver
        self.completelogo = driver.find_element(By.XPATH, Locator.completelogo)
        self.confirmationmsg = driver.find_element(By.XPATH, Locator.confirmationmsg)
        self.backhome = driver.find_element(By.XPATH, Locator.backhome)

    def getcompletelogo(self):
        return self.completelogo

    def getconfirmationmsg(self):
        return self.confirmationmsg

    def getbackhome(self):
        return self.backhome