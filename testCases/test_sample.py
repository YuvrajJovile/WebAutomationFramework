import pytest
from pageObjects.BasePage import BasePage
from utilities.baseUtility import BaseUtility

class Test_Sample(BaseUtility):

    search_Text_reg = "Tree"
    search_Text_san = "Dog"
    baseURL = "https://www.google.com/search?q=a"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_sample_baseTest_regression(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_001 *****************")
        self.logData.info("****Started  Sample test ****")
        self.logData.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.basePage = BasePage(self.driver)
        self.basePage.setSearchText(self.search_Text_reg)
        self.basePage.clickSearch()
        assert self.basePage.getTitle().is_displayed()

    @pytest.mark.regression
    def test_sample_baseTest_sanity(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_002 *****************")
        self.logData.info("****Started  Sample test ****")
        self.driver.get(self.baseURL)
        self.logData.info("****Opening URL****")
        self.basePage = BasePage(self.driver)
        self.basePage.setSearchText(self.search_Text_san)
        self.basePage.clickSearch()
        assert self.basePage.getTitle().is_displayed()