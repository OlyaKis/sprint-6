from selenium.webdriver.common.keys import Keys
from locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('open base page')
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
        self.wait_for_elements(OrderPageLocators.METRO_OPTION)
        options = self.find_elements(OrderPageLocators.METRO_OPTION)
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
        self.wait_for_elements(OrderPageLocators.RENTAL_PERIOD_OPTION)
        options = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTION)
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
        self.click_with_action_chains(OrderPageLocators.YANDEX_LOGO, modifier=Keys.CONTROL)

    @allure.step('click samokat logo')
    def click_logo_samokat(self):
        self.click_element(OrderPageLocators.SAMOKAT_LOGO)

    @allure.step('Assert current URL')
    def assert_current_url(self, expected_url):
        current_url = self.get_current_url()
        assert current_url == expected_url

    @allure.step('Switch to new window')
    def switch_to_window(self):
        self.switch_to_new_window()

    @allure.step('Verify URL contains')
    def verify_url_contains(self, expected_url):
        self.wait_for_url_change(expected_url)
        assert expected_url in self.get_current_url()
