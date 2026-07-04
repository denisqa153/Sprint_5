from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import NavigationLocators, Autorization, Input, Registration
EXPECTED_ERROR_COLOR = "255, 105, 114"


def test_registration_user_no_email_mask(driver):
    random_number = random.randint(100,999)
    domains = ["gmail.com", "yandex.ru", "mail.ru", "rambler.ru"]
    random_domains = random.choice(domains)
    new_email = f'user{random_number}{random_domains}'





#кнопка "Вход/регистрация"
    driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

#ожидание пока появится кнопка
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(Autorization.NOT_ACCOUNT_BUTTON))


#кнопка "Нет аккаунта"
    driver.find_element(*Autorization.NOT_ACCOUNT_BUTTON).click()

#ввод эмейла
    driver.find_element(*Input.INPUT_EMAIL).send_keys(new_email)



#нажать ккнопку "Создать аккаунт"
    WebDriverWait(driver, 5).until(
    expected_conditions.element_to_be_clickable(Registration.CREATE_ACCOUNT_BUTTON)
).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Ошибка']"))
    )
  
    error_email = driver.find_element(By.XPATH,"//span[text()='Ошибка']")
    assert error_email.text == 'Ошибка'

    error_red_email = driver.find_element(By.XPATH, "//input[@name='email']/parent::div")
    border_color = error_red_email.value_of_css_property("border-top-color")
    assert EXPECTED_ERROR_COLOR in border_color, f"Цвет рамки не красный! Фактический цвет: {border_color}"


    error_red_password = driver.find_element(By.XPATH, "//input[@name='password']/parent::div")
    border_color_password = error_red_password.value_of_css_property("border-top-color")
    assert EXPECTED_ERROR_COLOR in border_color_password, f"Цвет рамки не красный! Фактический цвет: {border_color_password}"


    error_red_submitPassword = driver.find_element(By.XPATH, "//input[@name='submitPassword']/parent::div")
    border_color_submitPassword = error_red_submitPassword.value_of_css_property("border-top-color")
    assert EXPECTED_ERROR_COLOR in border_color_submitPassword, f"Цвет рамки не красный! Фактический цвет: {border_color_submitPassword}"

                                       