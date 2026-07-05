from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators, Autorization, Input, Advert, ProfilePage


class TestCreateAdvertAuth:
    """Класс, объединяющий тесты создания объявлений авторизованным пользователем"""

    def test_create_advert_auth_user(self, driver, create_user):  # ДОБАВЛЕН self
        user = create_user
        advert_name = "name"

        wait = WebDriverWait(driver, 5)

        # Авторизация
        driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(Input.INPUT_EMAIL)
        ).send_keys(user["email"])

        driver.find_element(*Input.INPUT_PASSWORD).send_keys(user["password"])
        driver.find_element(*Autorization.LOGIN_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(NavigationLocators.PROFIL_BUTTON)
        )

        # Создание объявления
        wait.until(
            EC.element_to_be_clickable(NavigationLocators.CREATE_ADVERT)
        ).click()

        wait.until(
            EC.visibility_of_element_located(Advert.INPUT_NAME)
        ).send_keys(advert_name)

        # Описание и цена
        wait.until(EC.presence_of_element_located(Advert.INPUT_DESCRIPTION))
        driver.find_element(*Advert.INPUT_DESCRIPTION).send_keys("description")
        driver.find_element(*Advert.INPUT_PRICE).send_keys("123")

        # Дропдаун города
        wait.until(
            EC.visibility_of_element_located(Advert.DROPDOWN_CITY_BUTTON)
        ).click()

        wait.until(
            EC.element_to_be_clickable(Advert.DROPDOWN_CITY_SELECT)
        ).click()

        # Дропдаун категории
        wait.until(
            EC.element_to_be_clickable(Advert.DROPDOWN_CATEGORY_BUTTON)
        ).click()

        wait.until(
            EC.element_to_be_clickable(Advert.DROPDOWN_CATEGORY_SELECT)
        ).click()

        # Радиобаттон и публикация
        driver.find_element(*Advert.RADIO_USED).click()
        driver.find_element(*Advert.PUBLISH_BUTTON).click()

        # Переход в профиль
        wait.until(
            EC.element_to_be_clickable(NavigationLocators.PROFIL_BUTTON)
        ).click()

        wait.until(
            EC.visibility_of_element_located(ProfilePage.MY_ADVERTS)
        )

        # Ждем, пока загрузятся и станут видимыми имена объявлений
        adverts = wait.until(EC.visibility_of_any_elements_located(ProfilePage.ALL_ADVERTS_NAMES))
        
        # Собираем текст из найденных элементов
        advert_names = [advert.text for advert in adverts]
        
        # Проверяем наличие нашего объявления
        assert advert_name in advert_names
