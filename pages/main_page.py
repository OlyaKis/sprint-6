from pages.base_page import BasePage
from locators import BasePageLocators
import allure


class MainPage(BasePage):

    @allure.step('open base page')
    def open_main_page(self):
        self.open_page()

    @allure.step('accept cookies')
    def click_cookie_button(self):
        self.click_element(BasePageLocators.COOKIE_BUTTON)

    @allure.step('click question')
    def click_question(self, question_locator):
        self.click_element(question_locator)

    @allure.step('click answer')
    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)
