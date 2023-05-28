from Cermati_Framework.PageObject.HomePage import HomePage
from Cermati_Framework.PageObject.ResultPage import ResultPage
from Cermati_Framework.Utilities.BaseClass import BaseClass
from time import sleep

class TestOne(BaseClass):

    def test_case2(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.send_search_text().send_keys("Macbook")
        log.info("Sent keys for Macbook")
        self.selectOptionByText(homepage.select_search_category(),"Computers/Tablets & Networking")
        homepage.click_search().click()
        log.info("Clicked on search button")
        resultpage = ResultPage(self.driver)
        result_text = resultpage.search_result_text().text
        assert "Macbook" in result_text, "Result doesn't match"

