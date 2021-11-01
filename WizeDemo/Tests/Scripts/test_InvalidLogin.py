import sys, os
import unittest, selenium
import json
import HtmlTestRunner
sys.path.insert(1, '../../')

from time import sleep
from selenium import webdriver
from PageObject.Locators import Locator
from PageObject.Pages.LoginPage import Login
from PageObject.TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Swang_InvalinLogin(WebDriverSetup):
 
    def test_Invalid_Page(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/")
        print("Opening page.... saucedemo.com.....")
        self.driver.set_page_load_timeout(30)


        with open('../../PageObject/Pagedata.json') as f:
            PageData = json.load(f)

        LogPage = Login(driver)
        web_title = PageData['PageTitle']

        if LogPage.getLogo().is_displayed():
            self.assertEqual(driver.title, web_title, "Name Page is not the expected")
            print(driver.title + " " + LogPage.getLogo().get_attribute('class') + "  is successfully displayed")
        else:
            print("\nPage is not loading")
            self.assertNotIn(web_title, driver.title, "Expected Web page name is not contained in web title")

        sleep(1)
        usrs = LogPage.getUsers().split()
        pwd = LogPage.getCredential().split()

        #Invalid Credentials
        invalidUser = PageData['InvalidCred'][0]['invalid']
        invalidPwd = PageData['InvalidCred'][0]['inpwd']

        sleep(1)
        LogPage.getUsername().send_keys(invalidUser)
        LogPage.getPassword().send_keys(invalidPwd)

        sleep(1)
        LogPage.getLogbutton().click()

        sleep(2)
        #Check if there is an error while logging
        error_login_message = "error-message-container error"
        if LogPage.getLoginError().get_attribute('class') == error_login_message:
            print("\nUnable to login with invalid credentials")

        sleep(1)
        self.assertIn(error_login_message,LogPage.getLoginError().get_attribute('class'), "No Expected Error Mesagge")

        print("\nTEST COMPLETED ...")

if __name__ == '__main__':
    #html_report_dir = ("../../Reports")
    #testRunner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    unittest.main()     
