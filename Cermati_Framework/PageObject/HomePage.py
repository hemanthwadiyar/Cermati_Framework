from selenium.webdriver.common.by import By

from Cermati_Framework.PageObject.ResultPage import ResultPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//button[@id='gh-shop-a']")
    category_select = (By.LINK_TEXT, "Cell phones & accessories")
    search_text = (By.XPATH,"//input[@aria-label='Search for anything']")
    search_category = (By.XPATH,"//select[@id='gh-cat']")
    search = (By.XPATH,"//input[@id='gh-btn']")
    def selectthecategory(self):
        return self.driver.find_element(*HomePage.shop)

    def shopbycategory(self):
        return self.driver.find_element(*HomePage.category_select)

    def send_search_text(self):
        return self.driver.find_element(*HomePage.search_text)

    def select_search_category(self):
        return self.driver.find_element(*HomePage.search_category)

    def click_search(self):
        return self.driver.find_element(*HomePage.search)







