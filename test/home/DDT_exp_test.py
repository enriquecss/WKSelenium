"""
Author: Enrique Decoss
@package test

Comments: always import related page from page folder
"""

from page.home.DDT_exp_page import GooglePage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class GoogleTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.gs = GooglePage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/enriquealejandro.d/PycharmProjects/WKSelenium/testsearch.csv"))
    @unpack
    def testSearch(self, searchCSV):
        self.gs.googleSearch(search=searchCSV)
        result2 = self.gs.verifySearch()
        self.ts.mark(result2, "Search Successfully")
        self.ts.markFinal("test_sanity_Google ", result2, "Google Search Successfully")

