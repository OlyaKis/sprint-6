from selenium.webdriver.common.by import By


class BasePageLocators:

    COOKIE_BUTTON = (By.XPATH, "//*[@id='rcc-confirm-button']")  # Кнопка согласия с куками
    QUESTION_PRICE = (By.XPATH, "//*[@id='accordion__heading-0']")  # Вопрос про цену и способы оплаты
    QUESTION_SEVERAL_SCOOTERS = (By.XPATH, "//div[@id='accordion__heading-1']")  # Вопрос про возможность заказать несколько самокатов
    QUESTION_TIME_RENT = (By.XPATH, "//div[@id='accordion__heading-2']")  # Вопрос про расчет времени аренды
    QUESTION_RENT_TODAY = (By.XPATH, "//div[@id='accordion__heading-3']")  # Вопрос про возможность заказать на сегодня
    QUESTION_CHANGE_RENT_TIME = (By.XPATH, "//div[@id='accordion__heading-4']")  # Вопрос про продление или возврат раньше
    QUESTION_CHARGER = (By.XPATH, "//div[@id='accordion__heading-5']")  # Вопрос про зарядное устройство
    QUESTION_CANCELLING = (By.XPATH, "//div[@id='accordion__heading-6']")  # Вопрос про возможность отмены заказа
    QUESTION_DELIVERY = (By.XPATH, "//div[@id='accordion__heading-7']")  # Вопрос про доставку за МКАД
    ANSWER_PRICE = (By.XPATH, "//*[@id='accordion__panel-0']")  # Ответ про цену и способы оплаты
    ANSWER_SEVERAL_SCOOTERS = (By.XPATH, "//div[@id='accordion__panel-1']")  # Ответ про возможность заказать несколько самокатов
    ANSWER_TIME_RENT = (By.XPATH, "//div[@id='accordion__panel-2']")  # Ответ про расчет времени аренды
    ANSWER_RENT_TODAY = (By.XPATH, "//div[@id='accordion__panel-3']")  # твет про возможность заказать на сегодня
    ANSWER_CHANGE_RENT_TIME = (By.XPATH, "//div[@id='accordion__panel-4']")  # Ответ про продление или возврат раньше
    ANSWER_CHARGER = (By.XPATH, "//div[@id='accordion__panel-5']")  # Ответ про зарядное устройство
    ANSWER_CANCELLING = (By.XPATH, "//div[@id='accordion__panel-6']")  # Ответ про возможность отмены заказа
    ANSWER_DELIVERY = (By.XPATH, "//div[@id='accordion__panel-7']")  # Ответ про доставку за МКАД


class OrderPageLocators:

    COOKIE_BUTTON = (By.XPATH, "//*[@id='rcc-confirm-button']")  # Кнопка согласия с куками
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")  # Яндекс логотип
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")  # Самокат логотип
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")  # Верхняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Нижняя кнопка "Заказать"
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле ввода имени
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле ввода фамилии
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле ввода адреса
    METRO_FIELD = (By.XPATH, "//input[contains(@class, 'select-search__input')]")  # Поле ввода метро
    METRO_OPTION = (By.CLASS_NAME, "select-search__option")  # Опции в выпадающем списке
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле ввода номера телефона
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # Кнопка перехода на следующую страницу
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле ввода даты доставки
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder']")  # Поле выпадающего списка
    RENTAL_PERIOD_OPTION = (By.CLASS_NAME, "Dropdown-option")  # Опции в выпадающем списке аренды
    COLOR_CHECKBOX_BLACK = (By.XPATH, "//label[text()='чёрный жемчуг']")  #Чекбокс "Черный жемчуг"
    COLOR_CHECKBOX_GREY = (By.XPATH, "//label[text()='серая безысходность']")  # Чекбокс "Серая безысходность"
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле для комментария курьеру
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка "Заказать"
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")  # Кнопка для подтверждения заказа
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")  # Сообщение об успешном заказе
