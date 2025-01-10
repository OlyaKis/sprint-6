import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
