from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('open base bage')
    def open_page(self):
        self.driver.get(self.URL)

    @allure.step('click top order button')
    def order_button_top(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step('click bottom order button')
    def order_button_bottom(self):
        self.click_element(OrderPageLocators.COOKIE_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('fill name')
    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)

    @allure.step('fill surname')
    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('fill address')
    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('choose metro station')
    def select_metro_station(self, station_name):
        self.click_element(OrderPageLocators.METRO_FIELD)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(OrderPageLocators.METRO_OPTION))
        options = self.driver.find_elements(*OrderPageLocators.METRO_OPTION)
        for option in options:
            if station_name in option.text:
                option.click()
                return

    @allure.step('fill phone')
    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('click next step button')
    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('choose date')
    def fill_date(self, date):
        self.click_element(OrderPageLocators.DATE_FIELD)
        self.send_keys_to_element(OrderPageLocators.DATE_FIELD, date)
        self.click_element(OrderPageLocators.FREE_SPACE)

    @allure.step('choose period')
    def select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTION))
        options = self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_OPTION)
        for option in options:
            if period in option.text:
                option.click()
                return

    @allure.step('choose color')
    def select_color(self, color):
        if color.lower() == "чёрный жемчуг":
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        elif color.lower() == "серая безысходность":
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_GREY)
        else:
            raise ValueError(f"Цвет '{color}' не найден!")

    @allure.step('text comment')
    def fill_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('press order button')
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('get success message')
    def get_success_message(self):
        return self.get_text_from_element(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step('click yandex logo button')
    def click_yandex_logo(self):
        logo = self.driver.find_element(*OrderPageLocators.YANDEX_LOGO)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(logo).key_up(Keys.CONTROL).perform()

    @allure.step('check url in new window')
    def verify_url_contains(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))
        assert expected_url in self.driver.current_url

    @allure.step('click samokat logo')
    def click_logo_samokat(self):
        self.click_element(OrderPageLocators.SAMOKAT_LOGO)

    @allure.step('Switch to new window')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

    @allure.step('Verify URL contains')
    def verify_url_contains(self, expected_url, time=10):
        WebDriverWait(self.driver, time).until(EC.url_contains(expected_url))
        assert expected_url in self.driver.current_url

    @allure.step('Get current URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Assert current URL')
    def assert_current_url(self, expected_url):
        current_url = self.get_current_url()
        assert current_url == expected_url
