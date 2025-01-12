from pages.main_page import MainPage
from locators import BasePageLocators
import allure
import pytest


@allure.story('test faq')
class TestQuestionAndAnswers:
    @allure.feature('test FAQ questions and answers')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (BasePageLocators.QUESTION_PRICE, BasePageLocators.ANSWER_PRICE, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (BasePageLocators.QUESTION_SEVERAL_SCOOTERS, BasePageLocators.ANSWER_SEVERAL_SCOOTERS,
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (BasePageLocators.QUESTION_TIME_RENT, BasePageLocators.ANSWER_TIME_RENT,
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (BasePageLocators.QUESTION_RENT_TODAY, BasePageLocators.ANSWER_RENT_TODAY, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (BasePageLocators.QUESTION_CHANGE_RENT_TIME, BasePageLocators.ANSWER_CHANGE_RENT_TIME,
         "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (BasePageLocators.QUESTION_CHARGER, BasePageLocators.ANSWER_CHARGER,
         "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (BasePageLocators.QUESTION_CANCELLING, BasePageLocators.ANSWER_CANCELLING,
         "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (BasePageLocators.QUESTION_DELIVERY, BasePageLocators.ANSWER_DELIVERY,
         "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    def test_question_and_answer(self, driver, question_locator, answer_locator, expected_answer):
        page = MainPage(driver)
        page.open_main_page()
        page.click_cookie_button()
        page.click_question(question_locator)
        actual_answer = page.get_answer_text(answer_locator)
        assert actual_answer == expected_answer
