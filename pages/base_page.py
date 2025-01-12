from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from constants import Constants
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = Constants.BASE_URL

    @allure.step('open base page')
    def open_page(self):
        self.driver.get(self.URL)

    @allure.step('Wait for elements to be visible')
    def wait_for_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    @allure.step('find element')
    def find_element(self, locator, time=10):
        by, value = locator
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((by, value)))

    @allure.step('Find elements on the page')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('click element')
    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()

    @allure.step('Send keys to element')
    def send_keys_to_element(self, locator, keys, time=10):
        element = self.find_element(locator, time)
        element.send_keys(keys)

    @allure.step('Wait for visibility of element')
    def wait_for_visibility(self, locator, time=10):
        element = self.find_element(locator, time)
        return element

    @allure.step('Get text from element')
    def get_text_from_element(self, locator, time=10):
        element = self.wait_for_visibility(locator, time)
        return element.text

    @allure.step("Get text of element with selector")
    def get_element_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    @allure.step('Switch to new window')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        self.driver.switch_to.window(new_window)

    @allure.step('Wait for URL to change')
    def wait_for_url_change(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url))

    @allure.step('Get current URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Click element with ActionChains")
    def click_with_action_chains(self, locator, modifier=None):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        if modifier:
            actions.key_down(modifier)
        actions.click(element)
        if modifier:
            actions.key_up(modifier)
        actions.perform()
