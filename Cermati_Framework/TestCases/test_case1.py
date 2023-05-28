import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Cermati_Framework.PageObject.HomePage import HomePage
from Cermati_Framework.PageObject.ResultPage import ResultPage
from Cermati_Framework.Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_case1(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.selectthecategory().click()
        log.info("Clicked on Shop by category")
        homepage.shopbycategory().click()
        log.info("Clicked on Cell Phone and Accessories")

        resultpage = ResultPage(self.driver)
        resultpage.select_category_filter().click()
        log.info("Clicked on Cell Phone accessories")
        resultpage.See_All().click()
        log.info("Clicked on See All")

        self.verifyElementPresence("//button[@aria-label='Close']")
        log.info("Waited for close button")

        resultpage.select_screen_size().click()
        log.info("Clicked on screensize filter")

        #self.verifyElementPresence("//label[@class='field__label field__label--end x-refine__multi-select-label']/span[text()='6 in or More']")
        resultpage.select_screen_size_value().click()
        log.info("Clicked on 6 in screen size option ")

        resultpage.select_item_location().click()
        log.info("Clicked on Location filter")
        resultpage.select_location().click()
        log.info("Clicked on location option")

        resultpage.select_price_filter().click()
        log.info("Clicked on Price filter")
        resultpage.enter_min_price().send_keys("200")
        log.info("Entered the minimum value")
        resultpage.enter_max_price().send_keys("300")
        log.info("Entered the Maximum value")

        resultpage.click_apply().click()
        log.info("Clicked on Apply button")

        resultpage.select_applied_filter().click()
        log.info("Clicked on applied filter to check the filters results")
        screen_size_text = resultpage.verify_screen_size_filter().text
        location_text = resultpage.verify_location_filter().text
        price_text = resultpage.verify_price_filter().text

        assert "6 in " in screen_size_text
        assert "200" and "300" in price_text
        assert "North America" in location_text





