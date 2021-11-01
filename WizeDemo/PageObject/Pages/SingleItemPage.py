import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class SingleItem(object):
    def __init__(self, driver):
        self.driver = driver
        self.cartLogo = driver.find_element(By.XPATH, Locator.cartLogo)
        self.cartOnesie = driver.find_element(By.XPATH, Locator.cartOnesie)
        self.itemPurchase = driver.find_element(By.XPATH, Locator.purchase)

    def getcartLogo(self):
        return self.cartLogo

    def getcartOnesie(self):
        return self.cartOnesie

    def getitemPurchase(self):
        return self.itemPurchase