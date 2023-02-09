from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasePage:

    # Sample generic elements
    search_text_box_xpath = "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input"
    search_button_xpath = "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/button/div/span"
    title = (By.CSS_SELECTOR, "h1")

    def __init__(self, driver):
        self.driver=driver

    def setSearchText(self, searchText):
        self.driver.find_element(By.XPATH, self.search_text_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_text_box_xpath).send_keys(searchText)

    def clickSearch(self):
        self. driver.find_element(By.XPATH, self.search_button_xpath).click()

    def getTitle(self):
        return self.driver.find_element(*BasePage.title)