import pytest
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators, Autorization, Registration, Input


@pytest.fixture
def driver():
    # SETUP: Код выполняется ДО старта теста
    browser = webdriver.Chrome()
    browser.get("https://qa-desk.education-services.ru/")

    yield browser  # Передаем браузер в тест

    browser.quit()



@pytest.fixture
def create_user(driver):
    random_number = random.randint(100, 999999)
    domains = ["gmail.com", "yandex.ru", "mail.ru", "rambler.ru"]

    new_email = f"user{random_number}@{random.choice(domains)}"
    password = "123456"

    # Регистрация
    driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(
            Autorization.NOT_ACCOUNT_BUTTON
        )
    ).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            Input.INPUT_EMAIL
        )
    ).send_keys(new_email)

    driver.find_element(*Input.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Input.INPUT_SECOND_PASSWORD).send_keys(password)

    driver.find_element(
        *Registration.CREATE_ACCOUNT_BUTTON
    ).click()

    # Ждем профиль
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h3[@class='profileText name']")
        )
    )

    # Выходим
    driver.find_element(
        By.XPATH,
        "//button[text()='Выйти']"
    ).click()

    # Ждем, что снова появилась кнопка входа
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            NavigationLocators.LOGIN_REG_BUTTON
        )
    )

    return {
        "email": new_email,
        "password": password,
    }