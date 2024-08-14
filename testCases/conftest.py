import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching chrome browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
        print("Launching edge browser.........")
    yield driver
    driver.quit()
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

