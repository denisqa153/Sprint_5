from selenium.webdriver.common.by import By
 #Элементы, которые видны на любой странице сайта
class NavigationLocators:
    #кнопка "Вход/регистрация"
    LOGIN_REG_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    #кнопка "Выход"
    EXIT_BUTTON = (By.CSS_SELECTOR, "button.btnSmall")
    #кнопка "Разместить объявление"
    CREATE_ADVERT = (By.CSS_SELECTOR, "button.buttonPrimary")
    #кнопка "Нет аккаутна"
    NOT_ACCOUNT = (By.CSS_SELECTOR, "buttonSecondary")
    #кнопка профиля (иконка аккаунта)
    PROFIL_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
class Autorization:
    #кнопка "Нет аккаунта"
    NOT_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    LOGIN_BUTTON = (By.XPATH, "//div/button[text() = 'Войти']")

class Registration:
    #кнопка "Создать аккаунт"
    CREATE_ACCOUNT_BUTTON =  (By.XPATH, "//button[@type='submit'][text()='Создать аккаунт']")
class Input:
    #поле эмейла
    INPUT_EMAIL = (By.NAME, "email")
    #поле пароля
    INPUT_PASSWORD = (By.NAME, "password")
    #поле повторно пароля
    INPUT_SECOND_PASSWORD = (By.NAME, "submitPassword")
class Advert:
    #поле название
    INPUT_NAME = (By.NAME, "name")
    #поле описание
    INPUT_DESCRIPTION = (By.CSS_SELECTOR, "textarea[name='description'][placeholder='Описание товара']"
)
    #поле стоимость
    INPUT_PRICE = (By.NAME, "price")
    #дропдаун кнопка города
# кнопка открытия списка городов
    DROPDOWN_CITY_BUTTON = (By.XPATH,"//input[@name='city']/following-sibling::button")    #дропдаун выбор города из списка
    DROPDOWN_CITY_SELECT = (By.XPATH, "//span[text()='Екатеринбург']/parent::button")   #дропдаун кнопка категории
   
    DROPDOWN_CATEGORY_BUTTON = (By.XPATH, "//div[./input[@name='category']]/button")
    #дропдаун выбор категории из списка
    DROPDOWN_CATEGORY_SELECT = (By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')][.//span[text()='Книги']]")

    #радиобатон Б/У
    RADIO_USED = (By.XPATH, "//fieldset[contains(@class, 'createListing_inputRadio')]//label[text()='Б/У']")
    #кнопка "Опубликовать"
    PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Опубликовать']")


class ProfilePage:
    """Локаторы для страницы профиля пользователя"""
    # заголовок страницы "Мои объявления"
    MY_ADVERTS = (By.XPATH, "//h1[text()='Мои объявления']")
    
    # общий контейнер, внутри которого лежат все карточки объявлений
    ALL_ADVERTS_NAMES = (By.CSS_SELECTOR, "div.card h2")
