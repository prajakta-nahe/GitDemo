

from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):    # setting driver from e2e test case to this constructor as an argument
        self.driver = driver             # creating driver object through constructor

    shop = (By.CSS_SELECTOR,"a[href*='shop']")      # declare as a tuple
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID,"exampleCheck1")
    dropdown = (By.ID,"exampleFormControlSelect1")
    submit = (By.XPATH,"//input[@type='submit']")
    alert = (By.CSS_SELECTOR,"[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()     # class variable , needs to be called by class name  # mark by * to be treated as tuple
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()   # extract first and second element from tuple by default forms like this
        # adding click here itself for optimization and creating checkout page object here and returning it so as to reduce seperate object creation in main test
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.dropdown)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert)