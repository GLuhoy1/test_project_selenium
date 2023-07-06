import pytest
from selenium import webdriver
import urllib3

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
    yield driver

    driver.close()
