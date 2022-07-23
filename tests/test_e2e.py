import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.mark.usefixtures("setup")  ---> commenting this since we shifted this to BaseClass
from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):                   # ----> Inheriting

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()  # removing object creation for next page by identifying the trigger point to open next page
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()
        # checkOutPage = CheckOutPage(self.driver)
        # cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")           # parent child traversal
        i = -1
        for card in cards :
            i = i + 1
            cardText = card.text
            log.info(cardText)                  # print(cardText)
            if cardText == "Blackberry" :
                # self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()   # parent child traversal   # add button
                checkOutPage.getCardFooter()[i].click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()           # checkout button


        confirmpage = checkOutPage.checkOutItems()
                # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()    # checkout button on next page

        log.info("Entering country name as ind")
        confirmpage.GetCountry().send_keys("ind")
                #self.driver.find_element(By.ID, "country").send_keys("ind")       # auto suggestive dropdown for country
        # time.sleep(5)                                                  # Takes time to pop up results
                #wait = WebDriverWait(self.driver, 10)                            # explicit wait
                #wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")              # calling explicit wait method  from base class, passing text parameter as India
        self.driver.find_element(By.LINK_TEXT, "India").click()              # click on India
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()             # purchase button
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        log.info("Text received from application is" +textMatch)
        assert ("Success! Thank you!" in textMatch)


