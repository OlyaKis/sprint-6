from pages.base_page import BasePage
import allure

@allure.story('test faq')
class TestQuestionAndAnswers():
    @allure.feature('test price question')
    def test_price_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_price_question()
        answer = page.get_price_answer()
        assert answer == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.feature('test several scooter question')
    def test_several_scooter_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_several_scooter_question()
        answer = page.get_several_scooter_answer()
        assert answer == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.feature('test time rent question')
    def test_time_rent_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_time_rent_question()
        answer = page.get_time_rent_answer()
        assert answer == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.feature('test rent today question')
    def test_rent_today_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_rent_today_question()
        answer = page.get_rent_today_answer()
        assert answer == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.feature('test change rent time question')
    def test_change_rent_time_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_change_rent_time_question()
        answer = page.get_change_rent_time_answer()
        assert answer == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.feature('test charger question')
    def test_charger_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_charger_question()
        answer = page.get_charger_answer()
        assert answer == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.feature('test cancelling question')
    def test_cancelling_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_cancelling_question()
        answer = page.get_cancelling_answer()
        assert answer == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.feature('test delivery question')
    def test_delivery_question(self, driver):
        page = BasePage(driver)
        page.open_page()
        page.click_delivery_question()
        answer = page.get_delivery_answer()
        assert answer == "Да, обязательно. Всем самокатов! И Москве, и Московской области."