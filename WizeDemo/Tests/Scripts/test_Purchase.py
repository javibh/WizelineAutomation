import sys, os, random
import unittest, selenium
import HtmlTestRunner
sys.path.insert(1, '../../')

from time import sleep
from selenium import webdriver
from PageObject.Locators import Locator
from PageObject.Pages.LoginPage import Login 
from PageObject.Pages.ProductPage import Product 
from PageObject.Pages.SingleItemPage import SingleItem 
from PageObject.Pages.CheckoutPage import Checkout 
from PageObject.Pages.OverviewPage import Overview 
from PageObject.Pages.OrderCompletePage import CompleteOrder 
from PageObject.TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Swang_Purchase(WebDriverSetup):

    def test_Purchase_Item(self):
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

        sleep(1)
        ProductPage = Product(driver)
        if ProductPage.getappLogo().is_displayed():
            print("\nLogging successful - We are in Product Page section")

        sleep(1)
        print("\nAdding Products to Car List")
        item1 = (ProductPage.getP_onesie().get_attribute("id"))
        ProductPage.getP_onesie().click()

        sleep(1)
        print("\nCar List Ready")
        car_list = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        list_item = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        list_item.click()

        sleep(1)
        print("\nMove to CART list")
        SingleList = SingleItem(driver)
        pageListtitle_cart = "YOUR CART"
        if SingleList.getcartLogo().text == pageListtitle_cart:
            print("\nCart List is Displayed")
        self.assertEqual(pageListtitle_cart, SingleList.getcartLogo().text, "Checkout page is not displayed") 

        sleep(1)
        List1 = (SingleList.getcartOnesie().text)
        print(List1)

        sleep(1)
        SingleList.getitemPurchase().click()

        sleep(1)
        print("\nConfirm purchase")
        CheckoutItem = Checkout(driver)
        pageListtitle_info = "CHECKOUT: YOUR INFORMATION"
        if CheckoutItem.getcheckoutlogo().text == pageListtitle_info:
            print("\nPurchasing Page is Displayed")
        self.assertEqual(pageListtitle_info, CheckoutItem.getcheckoutlogo().text, "Checkout page is not displayed") 

        sleep(1)
        print("\nAdding Personal Info")
        CheckoutItem.getinfoname().send_keys("Wizeline")
        CheckoutItem.getinfolastname().send_keys("Zapopan")
        CheckoutItem.getinfozip().send_keys("123")
        CheckoutItem.getconfirmshop().click()

        sleep(1)
        print("\nInformation Overview and complete order")
        OverviewInfo = Overview(driver)
        pageListtitle_overview= "CHECKOUT: OVERVIEW"
        if OverviewInfo.getoverviewlogo().text == pageListtitle_overview:
            print("\nOverview Page is Displayed")
        self.assertEqual(pageListtitle_overview, OverviewInfo.getoverviewlogo().text, "Checkout page is not displayed") 

        sleep(1)
        print("\nVerify if Information is propertly display")
        OverviewInfo.getoverviewitem().is_displayed()
        OverviewInfo.getitemprice().is_displayed()
        OverviewInfo.getpaymentinfo().is_displayed()
        OverviewInfo.getshipinfo().is_displayed()
        OverviewInfo.gettotalprice().is_displayed()
 
 
        print(OverviewInfo.gettotalprice().text)
        print(OverviewInfo.getoverviewitem().text)
        Final_list1 = OverviewInfo.getoverviewitem().text
        print(OverviewInfo.getpaymentinfo().text)
        print(OverviewInfo.getshipinfo().text)
        self.assertEqual(List1, Final_list1, "Item added is not in the final confimation list")


        sleep(1)
        print("\nPressing Finish")
        OverviewInfo.getfinishshop().click()
        finish = CompleteOrder(driver)
        pageListtitle_checkout = "CHECKOUT: COMPLETE!"
        if finish.getcompletelogo().text == pageListtitle_checkout:
            print("\nComplete Page is Displayed")
        self.assertEqual(pageListtitle_checkout, finish.getcompletelogo().text, "Checkout page is not displayed")    

        sleep(1)
        print("\nGo back to home page")
        finish.getconfirmationmsg().is_displayed()
        finish.getbackhome().click()
        print("\nTEST COMPLETED ...")

if __name__ == '__main__':
    html_report_dir = ("../../Reports")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))    