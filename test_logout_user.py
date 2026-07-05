from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators, Autorization, Input


class TestLogin:
    """Класс, объединяющий тесты функционала авторизации"""

    def test_login(self, driver, create_user): 
        user_data = create_user

        # Кнопка "Вход/регистрация"
        driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

        # Ожидание пока появится поле email
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Input.INPUT_EMAIL)
        )

        # Ожидание пока появится поле password
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Input.INPUT_PASSWORD)
        )

        # Ввод эмейла и пароля
        driver.find_element(*Input.INPUT_EMAIL).send_keys(user_data["email"])
        driver.find_element(*Input.INPUT_PASSWORD).send_keys(user_data["password"])

        # Нажать на кнопку входа
        driver.find_element(*Autorization.LOGIN_BUTTON).click()

        # Ожидаем прогрузки кнопки выйти и клик по ней
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(NavigationLocators.EXIT_BUTTON)
        ).click()

        # Ожидаем пока исчезнет аватар
        avatar_is_gone = WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "div.flexRow button svg"))
        )
        assert avatar_is_gone, "Аватар пользователя всё ещё отображается после нажатия кнопки Выйти!"

        # Ожидаем пока исчезнет имя пользователя
        username_is_gone = WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, "//h3[@class = 'profileText name']"))
        )
        assert username_is_gone

        # Ожидаем появление кнопки "Вход/регистрация"
        login_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(NavigationLocators.LOGIN_REG_BUTTON)
        )
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не появилась!"
