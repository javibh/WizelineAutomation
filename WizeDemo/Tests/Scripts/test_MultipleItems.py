import sys, os, random
import unittest, selenium
import HtmlTestRunner
sys.path.insert(1, '../../')

from time import sleep
from selenium import webdriver
from PageObject.Locators import Locator
from PageObject.Pages.LoginPage import Login 
from PageObject.Pages.ProductPage import Product 
from PageObject.Pages.CartListPage import Cart 
from PageObject.TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Swang_MultItems(WebDriverSetup):

    def test_Multiple_Item(self):
        driver = self.driver
        LogPage = Login(driver)

        sleep(1)
        usrs = LogPage.getUsers().split()
        pwd = LogPage.getCredential().split()

        #Valid Credentials
        validUser = usrs[3]
        validPwd = pwd[4]

  
        sleep(1)
        print("Testing Credentials " + validUser + " and " + validPwd)
        LogPage.getUsername().send_keys(validUser)
        LogPage.getPassword().send_keys(validPwd)

        sleep(1)
        LogPage.getLogbutton().click()

        sleep(1)
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
        print("\nAdding Products to Car List")
        item1 = (ProductPage.getP_onesie().get_attribute("id")).lower()
        item2 = (ProductPage.getP_bike_light().get_attribute("id")).lower()
        item3 = (ProductPage.getP_backpack().get_attribute("id")).lower()

        ProductPage.getP_onesie().click()
        ProductPage.getP_bike_light().click()
        ProductPage.getP_backpack().click()

        sleep(1)
        print("\nCar List Ready")
        car_list = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        list_items = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        list_items.click()

        sleep(1)
        CartPage = Cart(driver)
        pagetitle = "YOUR CART"
        if CartPage.getcartLogo().text == pagetitle:
            print("\nCart List is Displayed")
        self.assertEqual(CartPage.getcartLogo().text, pagetitle)

        sleep(1)
        List1 = (CartPage.getcartOnesie().text).lower().split()[-1]
        List2 = (CartPage.getcartbike_ligh().text).lower().split()[-1]
        List3 = (CartPage.getcartbackpack().text).lower().split()[-1]

        #Asserts
        self.assertIn(List1, item1, "Item added in not listed in Cart list")
        self.assertIn(List2, item2, "Item added in not listed in Cart list")
        self.assertIn(List3, item3, "Item added in not listed in Cart list")

        sleep(1)
        print("\nMoving back to shopping page")
        CartPage.getconti_shopping().click()
        print("\nTEST COMPLETED ...")

if __name__ == '__main__':
    html_report_dir = ("../../Reports")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))    