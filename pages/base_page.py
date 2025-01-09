from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('open base page')
    def open_page(self):
        self.driver.get(self.URL)

    @allure.step('find element')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step('click price question')
    def click_price_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(BasePageLocators.QUESTION_PRICE))
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_PRICE)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_PRICE))

    @allure.step('click several scooters question')
    def click_several_scooter_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_SEVERAL_SCOOTERS)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_SEVERAL_SCOOTERS))

    @allure.step('click rent question')
    def click_time_rent_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_TIME_RENT)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_TIME_RENT))

    @allure.step('click rent today question')
    def click_rent_today_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_RENT_TODAY)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_RENT_TODAY))

    @allure.step('click change rent time question')
    def click_change_rent_time_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_CHANGE_RENT_TIME)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_CHANGE_RENT_TIME))

    @allure.step('click charger question')
    def click_charger_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_CHARGER)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_CHARGER))

    @allure.step('click cancelling question')
    def click_cancelling_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_CANCELLING)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_CANCELLING))

    @allure.step('click delivery question')
    def click_delivery_question(self):
        cookie = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie.click()
        question_price = self.driver.find_element(*BasePageLocators.QUESTION_DELIVERY)
        question_price.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(BasePageLocators.ANSWER_DELIVERY))

    @allure.step('get price answer')
    def get_price_answer(self):
        answer_price = self.driver.find_element(*BasePageLocators.ANSWER_PRICE)
        return answer_price.text

    @allure.step('get several scooter answer')
    def get_several_scooter_answer(self):
        answer_several_scooters = self.driver.find_element(*BasePageLocators.ANSWER_SEVERAL_SCOOTERS)
        return answer_several_scooters.text

    @allure.step('get time rent answer')
    def get_time_rent_answer(self):
        answer_time_rent = self.driver.find_element(*BasePageLocators.ANSWER_TIME_RENT)
        return answer_time_rent.text

    @allure.step('get rent today answer')
    def get_rent_today_answer(self):
        answer_rent_today = self.driver.find_element(*BasePageLocators.ANSWER_RENT_TODAY)
        return answer_rent_today.text

    @allure.step('get change rent time answer')
    def get_change_rent_time_answer(self):
        answer_change_rent_time = self.driver.find_element(*BasePageLocators.ANSWER_CHANGE_RENT_TIME)
        return answer_change_rent_time.text

    @allure.step('get charger answer')
    def get_charger_answer(self):
        answer_charger = self.driver.find_element(*BasePageLocators.ANSWER_CHARGER)
        return answer_charger.text

    @allure.step('get cancelling answer')
    def get_cancelling_answer(self):
        answer_cancelling = self.driver.find_element(*BasePageLocators.ANSWER_CANCELLING)
        return answer_cancelling.text

    @allure.step('get delivery answer')
    def get_delivery_answer(self):
        answer_delivery = self.driver.find_element(*BasePageLocators.ANSWER_DELIVERY)
        return answer_delivery.text
