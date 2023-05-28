from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    category_filter = (By.LINK_TEXT, "Cell Phones & Smartphones")
    view_all = (By.XPATH,"//section[contains(@class,'b-module b-carousel b-guidance b-display--landscape')]//span[contains(text(),'See All')]")
    screen_size = (By.XPATH,"//div[@class='x-overlay__wrapper--left']//div[@role='tab']/span[text()='Screen Size']")
    screen_size_value = (By.XPATH,"//label[@class='field__label field__label--end x-refine__multi-select-label']/span[text()='6 in or More']")
    item_location = (By.XPATH,"//div[@class='x-overlay__wrapper--left']//div[@role='tab']/span[text()='Item Location']")
    location = (By.XPATH,"//span/input[@value='North America']")
    price = (By.XPATH,"//div[@class='x-overlay__wrapper--left']//div[@role='tab']/span[text()='Price']")
    min_price = (By.XPATH,"//input[contains(@aria-label,'Minimum Value, US Dollar')]")
    max_price = (By.XPATH,"//input[contains(@aria-label,'Maximum Value, US Dollar')]")
    apply = (By.XPATH,"//button[@aria-label='Apply']")
    applied_filter = (By.XPATH,"//button/span[contains(text(),'applied')]")
    screen_size_filter = (By.XPATH,'''//*[@id="s0-27_1-9-0-1[0]-0-0-6-5-4[0]-flyout"]/div/ul/li[1]/a/span[1]''')
    location_filter = (By.XPATH, '''//*[@id="s0-27_1-9-0-1[0]-0-0-6-5-4[0]-flyout"]/div/ul/li[3]/a/span[1]''')
    price_filter = (By.XPATH, '''//*[@id="s0-27_1-9-0-1[0]-0-0-6-5-4[0]-flyout"]/div/ul/li[2]/a/span[1]''')
    search_result = (By.XPATH,'''//*[@id="item4d8cbf0397"]//a//span[@class='BOLD']''')
    def select_category_filter(self):
        return self.driver.find_element(*ResultPage.category_filter)

    def See_All(self):
        return self.driver.find_element(*ResultPage.view_all)

    def select_screen_size(self):
        return self.driver.find_element(*ResultPage.screen_size)

    def select_screen_size_value(self):
        return self.driver.find_element(*ResultPage.screen_size_value)

    def select_item_location(self):
        return self.driver.find_element(*ResultPage.item_location)

    def select_location(self):
        return self.driver.find_element(*ResultPage.location)

    def select_price_filter(self):
        return self.driver.find_element(*ResultPage.price)

    def enter_min_price(self):
        return self.driver.find_element(*ResultPage.min_price)

    def enter_max_price(self):
        return self.driver.find_element(*ResultPage.max_price)

    def click_apply(self):
        return self.driver.find_element(*ResultPage.apply)

    def select_applied_filter(self):
        return self.driver.find_element(*ResultPage.applied_filter)

    def verify_screen_size_filter(self):
        return self.driver.find_element(*ResultPage.screen_size_filter)

    def verify_price_filter(self):
        return self.driver.find_element(*ResultPage.price_filter)

    def verify_location_filter(self):
        return self.driver.find_element(*ResultPage.location_filter)

    def search_result_text(self):
        return self.driver.find_element(*ResultPage.search_result)








