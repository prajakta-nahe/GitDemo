import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None                               # declaring driver globally to None so as to resolve error in last driver object in screenshot method
def pytest_addoption(parser):     # command line options for specifying browser through cmd   # keyvalue = browsername
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope = "class")
def setup(request):                   # request instance                     # fixture to invoke the browser
    global driver
    browser_name = request.config.getoption("browser_name")                  # to retrieve browser name fom command prompt
    if browser_name == "chrome":
        service_obj = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj2 = Service("C:\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj2)

    elif browser_name == "ie":
        service_obj3 = Service("C:\\IEDriverServer.exe")
        driver = webdriver.IE(service=service_obj3)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver             # so as to return driver object since # return and yield can't be used together
    # return driver                         # driver being returned in the fixture will be sent to class object
    yield
    driver.close()                          # Teardown method to be executed at the end of test



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)