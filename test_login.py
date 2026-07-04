from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators, Autorization, Input


def test_login(driver, create_user):
    expected_result_username = "User."
    user_data = create_user

    # кнопка "Вход/регистрация"
    driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

    # ожидание пока появится поле email
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Input.INPUT_EMAIL)
    )

    # ожидание пока появится поле password
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            Input.INPUT_PASSWORD
        )
    )

    # ввод эмейла и пароля
    driver.find_element(*Input.INPUT_EMAIL).send_keys(user_data["email"])
    driver.find_element(*Input.INPUT_PASSWORD).send_keys(user_data["password"])

    driver.find_element(*Autorization.LOGIN_BUTTON).click()

    # ожидаем прогрузки страницы профиля
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h3[@class='profileText name']")
        )
    )

    # сравниваем ОР и ФР
    actual_result_username = driver.find_element(
        By.XPATH, "//h3[@class='profileText name']"
    ).text
    assert actual_result_username == expected_result_username

    avatar_content = driver.find_element(
        By.CSS_SELECTOR, "div.flexRow button svg"
    )

    # Проверяем, что иконка отображается на экране
    assert (
        avatar_content.is_displayed()
    ), "Дефолтный аватар (тег <svg>) не отображается!"
