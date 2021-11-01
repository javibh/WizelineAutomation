import sys, os, random
import unittest, selenium
import HtmlTestRunner
sys.path.insert(1, '../../')

from time import sleep
from selenium import webdriver
from PageObject.Locators import Locator
from PageObject.Pages.LoginPage import Login 
from PageObject.Pages.ProductPage import Product 
from PageObject.TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Swang_Navigate(WebDriverSetup):

    def test_Navigate_Page(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/")
        print("Opening page.... saucedemo.com.....")
        self.driver.set_page_load_timeout(30)

        LogPage = Login(driver)
        web_title = "Swag Labs"

        if LogPage.getLogo().is_displayed() and (driver.title == web_title):
            self.assertEqual(driver.title,web_title)
            print(driver.title + " " + LogPage.getLogo().get_attribute('class') + "  is successfully displayed")
        else:
            print("Page is not loading")

        sleep(1)
        usrs = LogPage.getUsers().split()
        pwd = LogPage.getCredential().split()

        #Valid Credentials
        validUser = random.choice(usrs[3:6])
        validPwd = pwd[4]

  
        sleep(1)
        print("Testing Credentials " + validUser + " and " + validPwd)
        LogPage.getUsername().send_keys(validUser)
        LogPage.getPassword().send_keys(validPwd)

        sleep(1)
        LogPage.getLogbutton().click()

        sleep(2)
        #Check if there is an error while logging
        try:
            if LogPage.getLoginError().get_attribute('class') == "error-message-container error":
                print("Unable to login with credentials provided, please review them")
                return
        except Exception:
            print("We don't see a error logging with current credentials")

        ProductPage = Product(driver)
        if ProductPage.getappLogo().is_displayed():
            print("\nLogging successful - We are in Product Page section")

        sleep(1)
        print("\nPrices are ordered from low to high value")
        ProductPage.getfilterprice_lh().click()
        sleep(1)
        print("\nTEST COMPLETED ...")

if __name__ == '__main__':
    html_report_dir = ("../../Reports")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))    