import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class Cart(object):
    def __init__(self, driver):
        self.driver = driver
        self.cartLogo = driver.find_element(By.XPATH, Locator.cartLogo)
        self.cartOnesie = driver.find_element(By.XPATH, Locator.cartOnesie)
        self.cartbike_ligh = driver.find_element(By.XPATH, Locator.cartbike_light)
        self.cartbackpack = driver.find_element(By.XPATH, Locator.cartbackpack)
        self.conti_shopping = driver.find_element(By.XPATH, Locator.conti_shopping)

    def getcartLogo(self):
        return self.cartLogo

    def getcartOnesie(self):
        return self.cartOnesie

    def getcartbike_ligh(self):
        return self.cartbike_ligh

    def getcartbackpack(self):
        return self.cartbackpack

    def getconti_shopping(self):
        return self.conti_shopping

