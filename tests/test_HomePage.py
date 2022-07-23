import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):      # fixture data gets captured here, params gets captured,test runs that much times

        log = self.getLogger()
        homepage=HomePage(self.driver)
        log.info("Firstname is"+ getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])           # driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys("Prajakta")
        homepage.getEmail().send_keys(getData["email"])       # driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
        homepage.getCheckBox().click()                     # driver.find_element(By.ID,"exampleCheck1").click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])   # calll from utilities, pass locator and text as arguments
        homepage.submitForm().click()                      # driver.find_element(By.XPATH,"//input[@type='submit']").click()
        alertText = homepage.getSuccessMessage().text      # alertText = driver.find_element(By.CSS_SELECTOR,"[class='alert-success']").text
        assert ("Success" in alertText)
        self.driver.refresh()                               # so as to refresh the browser before passing next data sets


        # @pytest.fixture(params=[("Prajakta","abc@gmail.com","Female"), ("Pranav","xyz@gmail.com","Male")]) ---> passing tuple index
        #@pytest.fixture(params = HomePageData.test_HomePage_data)      # Calling the data by it's class name
                                # passing dictionary, keyvalues

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param



# it is a good practice to have separate packages for, tests, test data, utilities and page objects
# java -jar jenkins.war -httpPort-8080    -----> To run jenkins jar
# Jenkins ---> code for Execute Windows batch command       cd tests
#                                            py.test --browser_name chrome --html=C:\Users\Lenovo\PycharmProject\PythonSelfFramework\reports\reports.html

#      cd tests                         # replaced by jenkins environment variable $WORKSPACE
#      py.test --browser_name chrome --html=$WORKSPACE/reports/reports.html

#   For selecting browser at runtime check option in configure ----> This project is parameterized--> give choice parameter as browserName
#   ---> give choices as chrome , firefox, IE.....

# The run command without hard coding as   ---->     cd tests
#                                                    py.test --browser_name "%browserName%" --html=$WORKSPACE/reports/reports.html

# Command to create xml file for junit -->      cd tests
#                                               py.test --browser_name "%browserName%" --html=$WORKSPACE/reports/reports.html -v --junitxml="result.xml"

# Select 'post build action' as 'Publish JUnit test result report' ---> pass 'tests/*.xml' in test reports xml box