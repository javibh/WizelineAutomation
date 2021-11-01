import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class Overview(object):
    def __init__(self, driver):
        self.driver = driver
        self.overviewlogo = driver.find_element(By.XPATH, Locator.overviewlogo)
        self.overviewitem = driver.find_element(By.XPATH, Locator.overviewitem)
        self.itemprice= driver.find_element(By.XPATH, Locator.itemprice)
        self.paymentinfo = driver.find_element(By.XPATH, Locator.paymentinfo)
        self.shipinfo = driver.find_element(By.XPATH, Locator.shipinfo)
        self.totalprice = driver.find_element(By.XPATH, Locator.totalprice)
        self.finishshop = driver.find_element(By.XPATH, Locator.finishshop)

    def getoverviewlogo(self):
        return self.overviewlogo

    def getoverviewitem(self):
        return self.overviewitem

    def getitemprice(self):
        return self.itemprice

    def getpaymentinfo(self):
        return self.paymentinfo

    def getshipinfo(self):
        return self.shipinfo

    def gettotalprice(self):
        return self.totalprice

    def getfinishshop(self):
        return self.finishshop