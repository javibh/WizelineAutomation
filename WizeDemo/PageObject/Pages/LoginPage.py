import sys 
import os
sys.path.insert(1, '../../')

from selenium.webdriver.common.by import By
from PageObject.Locators import Locator

class Login(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element(By.XPATH, Locator.LoginLogo)
        self.username = driver.find_element(By.XPATH, Locator.Login_Username)
        self.password = driver.find_element(By.XPATH, Locator.Login_Password)
        self.Logbutton = driver.find_element(By.XPATH, Locator.Login_Button)
        self.Users = str(driver.find_element(By.XPATH, Locator.Login_Users).text)
        self.Credential = str(driver.find_element(By.XPATH, Locator.Login_Credentials).text)
        self.LogError = driver.find_element(By.XPATH, Locator.Login_Error)

    def getLogo(self):
        return self.logo

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getLogbutton(self):
        return self.Logbutton

    def getUsers(self):
        return self.Users

    def getCredential(self):
        return self.Credential

    def getLoginError(self):
        return self.LogError


