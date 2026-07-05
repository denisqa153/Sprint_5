from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators, Autorization, Input, Registration


class TestRegistrationExistingUser:
    """Класс, объединяющий тесты регистрации уже существующего пользователя"""

    EXPECTED_ERROR_COLOR = "255, 105, 114"

    def test_registration_existing_user(self, driver, create_user):  
        user_data = create_user

        # Кнопка "Вход/регистрация"
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(NavigationLocators.LOGIN_REG_BUTTON)
        ).click()

        # Кнопка "Нет аккаунта"
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Autorization.NOT_ACCOUNT_BUTTON)
        ).click()

        # Ждем появления формы регистрации
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Input.INPUT_SECOND_PASSWORD)
        )

        # Заполняем форму
        driver.find_element(*Input.INPUT_EMAIL).send_keys(user_data["email"])
        driver.find_element(*Input.INPUT_PASSWORD).send_keys(user_data["password"])
        driver.find_element(*Input.INPUT_SECOND_PASSWORD).send_keys(user_data["password"])

        # Нажать "Создать аккаунт"
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Registration.CREATE_ACCOUNT_BUTTON)
        ).click()

        # Ожидание появления сообщения об ошибке
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Ошибка']"))
        )

        error_email = driver.find_element(By.XPATH, "//span[text()='Ошибка']")
        assert error_email.text == "Ошибка"

        # Проверка рамки Email
        error_red_email = driver.find_element(By.XPATH, "//input[@name='email']/parent::div")
        border_color = error_red_email.value_of_css_property("border-top-color")
        assert (
            self.EXPECTED_ERROR_COLOR in border_color
        ), f"Цвет рамки не красный! Фактический цвет: {border_color}"

        # Проверка рамки пароля
        error_red_password = driver.find_element(By.XPATH, "//input[@name='password']/parent::div")
        border_color_password = error_red_password.value_of_css_property("border-top-color")
        assert (
            self.EXPECTED_ERROR_COLOR in border_color_password
        ), f"Цвет рамки не красный! Фактический цвет: {border_color_password}"

        # Проверка рамки повторного пароля
        error_red_submitPassword = driver.find_element(By.XPATH, "//input[@name='submitPassword']/parent::div")
        border_color_submitPassword = error_red_submitPassword.value_of_css_property("border-top-color")
        assert (
            self.EXPECTED_ERROR_COLOR in border_color_submitPassword
        ), f"Цвет рамки не красный! Фактический цвет: {border_color_submitPassword}"
