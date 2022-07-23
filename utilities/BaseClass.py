import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass :

    def verifyLinkPresence(self,text):

        wait = WebDriverWait(self.driver, 10)                                               # explicit wait
        wait.until(EC.presence_of_element_located((By.LINK_TEXT,text)))              # using text captured by test case so as to generalize


    def selectOptionByText(self,locator,text):
        dropdown = Select(locator)             # dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
        dropdown.select_by_visible_text(text)                   # #dropdown.select_by_index(0)
                                                                        # dropdown.select_by_value()

    def getLogger(self):  # since method is defined under class, need to pass self parameter
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger