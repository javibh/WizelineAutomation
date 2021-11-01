Host OS: Windows 10

Automation Tools:
Python version: 2.7.18
Packages Installed
pip install html-testRunner
pip install testtools (at the end, it is not used, it was just tested for parellel test execution)
pip install selenium

WebDriver folder contains(added to enviroment valiables):
chrome driver

Framework structure:
WizeDemo(main folder)
    |----PageObject(Folder)
    |    |--- Pages(Folder): Contains all the getters for each page under test, each getter calls different xpath Locator variable.
    |    |--- TestBase(Folder): Contains Setup Class to initialize webdriver.
    |    |--- Locators.py: Contains all xpath variables(POM)
    |    |--- Pagedata.json: Contains information from the page, we can pull from it different variables and compare with what we are obtaining from web elements at run time
    |
    |---- Reports(Folder): html report for each test executed
    |---- Tests(Folder): html report for each test executed
    |    |--- Scripts(Folder): Individual script for different case execution(Invalid user, valid login.. etc.)
    |    |--- TestSuite(Folder): Script to execute selected tests under Scripts.
    |
    |---- WebDrivers(Folder): Binary for the different webdrivers

References:
Since i didn't have experience with POM, I took as reference this tutorial https://www.lambdatest.com/blog/page-object-model-in-selenium-python/

Now, for execution, you can ru individual test scripts listed in "Scripts" FOLDER:

e.g. ...\WizeDemo\Tests\Scripts>test_InvalidLogin.py
--------------------------------------------------------------------------------------
Running tests...
----------------------------------------------------------------------
 test_Invalid_Page (__main__.Swang_InvalinLogin) ...

----------------------------------------------------------------------
Ran 1 test in 0:00:23

OK
Generating HTML reports...
..\..\Reports\TestResults___main__.Swang_InvalinLogin_2021-11-01_07-38-37.html
------------------------------------------------------------------------------------

Or execute TestRunner script contained in "TestSuite" FOLDER, i will execute all test scripts:

e.g. ..\WizeDemo\Tests\TestSuite>TestRunner.py

Running tests...
----------------------------------------------------------------------