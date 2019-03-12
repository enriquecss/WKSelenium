"""
Author: Enrique Decoss
@package page

Comments: Inheritance from seleniumDriver

Description: Focusing on splitting sections as following

    Section 1: Locators
    Section 2: Methods to find and sendkeys to locators
    Section 3: Implement Methods with data
    Section 4: Assertions and Verifies

"""

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class GooglePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search = "q"
    _search_btn = "btnK"
    _dummyclick = "lga"
    _lucky_btn2 = "gbqfbb"
    _results = "resultStats"
    _google = "//img[@title='30th Anniversary of the World Wide Web']"

    # ********************* Methods ************************************************************************************

    def clickSearch(self, search):
        self.waitForElement(locator=self._search, locatorType="name", timeout=15)
        self.sendKeys(search, locator=self._search, locatorType="name")

    def clickDummy(self):
        self.elementClick(locator=self._dummyclick, locatorType="id")

    def navigateToSearchBtn(self):
        self.elementClick(locator=self._search_btn, locatorType="name")


    # *************************** Implementation and Data **************************************************************

    def googleSearch(self, search):
        self.clickSearch(search)
        self.navigateToSearchBtn()
        time.sleep(2)

    # ************************* Assertions and Verifies ****************************************************************

    def verifySearch(self):
        self.waitForElement(locator=self._results, locatorType="id", timeout=10)
        result = self.isElementPresent(locator=self._results,
                                       locatorType="id")
        return result

    def startNew(self):
        self.elementClick(locator=self._google, locatorType="xpath")
        time.sleep(1)