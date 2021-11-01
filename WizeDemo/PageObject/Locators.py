# 29-10-2021 History Change - Locators.py - Autor: Javier Barbosa
#            This class is created to identify all locators for page https://www.saucedemo.com/
#            Adding Locators for Login, Home Page, Navigation, Products, Social Media Links

class Locator(object):

    #Login Page
    LoginLogo = '//*[@id="root"]/div/div[1]'
    Login_Username = '//*[@id="user-name"]'
    Login_Password = '//*[@id="password"]'
    Login_Button = '//*[@id="login-button"]'
    Login_Users = '//*[@id="login_credentials"]'
    Login_Credentials = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]'
    Login_Error = '//*[@id="login_button_container"]/div/form/div[3]'

    #Product Page
    AppLogo = '//*[@id="header_container"]/div[1]/div[2]/div'
    productname = '//*[@id="header_container"]/div[2]/span'
    dropdown = '//*[@id="react-burger-menu-btn"]'
    filterPriceLH = '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]'
    logout = '//*[@id="logout_sidebar_link"]'

    #Product Items
    onesie = '//*[@id="add-to-cart-sauce-labs-onesie"]'
    bike_light = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    backpack = '//*[@id="add-to-cart-sauce-labs-backpack"]'

    #Cart List
    cartLogo = '//*[@id="header_container"]/div[2]/span'
    cartOnesie = '//*[@id="item_2_title_link"]/div'
    cartbike_light = '//*[@id="item_0_title_link"]/div'
    cartbackpack = '//*[@id="item_4_title_link"]/div'
    conti_shopping = '//*[@id="continue-shopping"]'

    #Checkout
    purchase = '//*[@id="checkout"]'
    checkoutlogo = '//*[@id="header_container"]/div[2]/span'
    infoname = '//*[@id="first-name"]'
    infolastname = '//*[@id="last-name"]'
    infozip = '//*[@id="postal-code"]'
    confirmshop = '//*[@id="continue"]'

    #Information overview
    overviewlogo = '//*[@id="header_container"]/div[2]/span'
    overviewitem = '//*[@id="item_2_title_link"]/div'
    itemprice = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
    paymentinfo = '//*[@id="checkout_summary_container"]/div/div[2]/div[2]'
    shipinfo = '//*[@id="checkout_summary_container"]/div/div[2]/div[4]'
    totalprice = '//*[@id="checkout_summary_container"]/div/div[2]/div[7]'
    finishshop = '//*[@id="finish"]'

    #Order Completed
    completelogo = '//*[@id="header_container"]/div[2]/span'
    confirmationmsg = '//*[@id="checkout_complete_container"]/h2'
    backhome = '//*[@id="back-to-products"]'


