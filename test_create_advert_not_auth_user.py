from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators


class TestCreateAdvertNotAuth:
    """Класс, объединяющий тесты создания объявлений неавторизованным пользователем"""

    expected_result = 'Чтобы разместить объявление, авторизуйтесь'

    def test_create_advert_not_auth_user(self, driver):
        # Нажать на кнопку "Создать объявление"
        driver.find_element(*NavigationLocators.CREATE_ADVERT).click()

        # Дождаться появления текста
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[@class='h1']"))
        )
        actual_result = driver.find_element(By.XPATH, "//h1[@class='h1']").text
        assert actual_result == self.expected_result
