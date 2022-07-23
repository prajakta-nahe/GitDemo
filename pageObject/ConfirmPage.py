from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    country = (By.ID,"country")

    def GetCountry(self):
        return self.driver.find_element(*ConfirmPage.country)