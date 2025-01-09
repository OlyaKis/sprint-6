import allure
import pytest
from pages.order_page import OrderPage

@allure.story('test orders scooters')
class TestOrderScooters:
    @allure.feature('test top order button')
    @pytest.mark.parametrize("name, surname, address, metro_station, phone, date, rental_period, color, comment", [
        ("Иван", "Иванов", "ул. Пушкина, д. 1", "Черкизовская", "+79991112233", "12.01.2025", "сутки", "чёрный жемчуг",
         "Позвонить за 10 минут до прибытия"),
        ("Анна", "Смирнова", "ул. Ленина, д. 5", "Сокольники", "+79998887766", "15.01.2025", "двое суток", "серая безысходность",
         "Не звонить, оставить у двери"),
    ])
    def test_order_scooter_top_button(self, driver, name, surname, address, metro_station, phone, date, rental_period, color, comment):
        page = OrderPage(driver)
        page.open_page()
        page.order_button_top()
        page.fill_name(name)
        page.fill_surname(surname)
        page.fill_address(address)
        page.select_metro_station(metro_station)
        page.fill_phone(phone)
        page.click_next()
        page.fill_date(date)
        page.select_rental_period(rental_period)
        page.select_color(color)
        page.fill_comment(comment)
        page.submit_order()
        success_message = page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.feature('test bottom order button')
    @pytest.mark.parametrize("name, surname, address, metro_station, phone, date, rental_period, color, comment", [
        ("Иван", "Иванов", "ул. Пушкина, д. 1", "Черкизовская", "+79991112233", "12.01.2025", "сутки", "чёрный жемчуг",
         "Позвонить за 10 минут до прибытия"),
        ("Анна", "Смирнова", "ул. Ленина, д. 5", "Сокольники", "+79998887766", "15.01.2025", "двое суток",
         "серая безысходность",
         "Не звонить, оставить у двери"),
    ])
    def test_order_scooter_bottom_button(self, driver, name, surname, address, metro_station, phone, date, rental_period,color, comment):
        page = OrderPage(driver)
        page.open_page()
        page.order_button_bottom()
        page.fill_name(name)
        page.fill_surname(surname)
        page.fill_address(address)
        page.select_metro_station(metro_station)
        page.fill_phone(phone)
        page.click_next()
        page.fill_date(date)
        page.select_rental_period(rental_period)
        page.select_color(color)
        page.fill_comment(comment)
        page.submit_order()
        success_message = page.get_success_message()
        assert "Заказ оформлен" in success_message

@allure.story('test buttons logo')
class TestButtonsLogo:
    @allure.feature('test samokat logo')
    def test_samokat_logo(self, driver):
        page = OrderPage(driver)
        page.open_page()
        page.order_button_top()
        page.click_logo_samokat()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.feature('test yandex logo')
    def test_yandex_logo(self, driver):
        page = OrderPage(driver)
        page.open_page()
        page.order_button_top()
        page.click_yandex_logo()
        page.switch_to_new_window()
        expected_url = "https://dzen.ru/"
        page.verify_url_contains(expected_url)
