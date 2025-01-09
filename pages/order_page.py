from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import OrderPageLocators
import allure

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('open base bage')
    def open_page(self):
        self.driver.get(self.URL)

    @allure.step('click top order button')
    def order_button_top(self):
        order_button_top = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_TOP)
        order_button_top.click()

    @allure.step('click bottom order button')
    def order_button_bottom(self):
        cookie = self.driver.find_element(*OrderPageLocators.COOKIE_BUTTON)
        cookie.click()
        order_button_bottom = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_BOTTOM)
        order_button_bottom.click()

    @allure.step('fill name')
    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    @allure.step('fill surname')
    def fill_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    @allure.step('fill address')
    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step('choose metro station')
    def select_metro_station(self, station_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.METRO_FIELD))
        metro_field = self.driver.find_element(*OrderPageLocators.METRO_FIELD)
        metro_field.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(OrderPageLocators.METRO_OPTION))
        options = self.driver.find_elements(*OrderPageLocators.METRO_OPTION)
        for option in options:
            if station_name in option.text:
                option.click()
                return

    @allure.step('fill phone')
    def fill_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)

    @allure.step('click next step button')
    def click_next(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('choose date')
    def fill_date(self, date):
        date_field = self.driver.find_element(*OrderPageLocators.DATE_FIELD)
        date_field.click()
        date_field.send_keys(date)
        self.driver.find_element(By.CSS_SELECTOR, "body").click()

    @allure.step('choose period')
    def select_rental_period(self, period):
        rental_dropdown = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_dropdown.click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTION))
        options = self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_OPTION)
        for option in options:
            if period in option.text:
                option.click()
                return

    @allure.step('choose color')
    def select_color(self, color):
        if color.lower() == "чёрный жемчуг":
            self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOX_BLACK).click()
        elif color.lower() == "серая безысходность":
            self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOX_GREY).click()
        else:
            raise ValueError(f"Цвет '{color}' не найден!")

    @allure.step('text comment')
    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step('press order button')
    def submit_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()

    @allure.step('get success message')
    def get_success_message(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE))
        return self.driver.find_element(*OrderPageLocators.SUCCESS_MESSAGE).text

    @allure.step('click yandex logo button')
    def click_yandex_logo(self):
        logo = self.driver.find_element(*OrderPageLocators.YANDEX_LOGO)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(logo).key_up(Keys.CONTROL).perform()

    @allure.step('switch to new window')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

    @allure.step('check url in new window')
    def verify_url_contains(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))
        assert expected_url in self.driver.current_url

    @allure.step('click samokat logo')
    def click_logo_samokat(self):
        go_to_samokat = self.driver.find_element(*OrderPageLocators.SAMOKAT_LOGO)
        go_to_samokat.click()

