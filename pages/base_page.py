from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators
from constants import Constants
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = Constants.BASE_URL

    @allure.step('open base page')
    def open_page(self):
        self.driver.get(self.URL)

    @allure.step('accept cookies')
    def accept_cookies(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()

    @allure.step('find element')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('click element')
    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Send keys to element')
    def send_keys_to_element(self, locator, keys, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        element.send_keys(keys)

    @allure.step('Wait for visibility of element')
    def wait_for_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Get text from element')
    def get_text_from_element(self, locator, time=10):
        element = self.wait_for_visibility(locator, time)
        return element.text

    @allure.step("Get text of element with selector")
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

