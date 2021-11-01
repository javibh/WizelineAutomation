import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class Product(object):
    def __init__(self, driver):
        self.driver = driver
        self.applogo = driver.find_element(By.XPATH, Locator.AppLogo)
        self.productname = driver.find_element(By.XPATH, Locator.productname)
        self.dropdown = driver.find_element(By.XPATH, Locator.dropdown)
        self.filterPricelh = driver.find_element(By.XPATH, Locator.filterPriceLH)
        self.P_onesie = driver.find_element(By.XPATH, Locator.onesie)
        self.P_bike_light = driver.find_element(By.XPATH, Locator.bike_light)
        self.P_backpack = driver.find_element(By.XPATH, Locator.backpack)

    def getappLogo(self):
        return self.applogo

    def getproductname(self):
        return self.productname

    def getdropdown(self):
        return self.dropdown

    def getfilterprice_lh(self):
        return self.filterPricelh

    def getP_onesie(self):
        return self.P_onesie

    def getP_bike_light(self):
        return self.P_bike_light
        
    def getP_backpack(self):
        return self.P_backpack
