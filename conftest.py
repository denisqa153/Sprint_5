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

    # Открыть окно входа
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            NavigationLocators.LOGIN_REG_BUTTON
        )
    ).click()

    # Перейти к регистрации
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            Autorization.NOT_ACCOUNT_BUTTON
        )
    ).click()

    # Ждем появления всех полей
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(Input.INPUT_SECOND_PASSWORD)
    )

    # Заполняем форму
    driver.find_element(*Input.INPUT_EMAIL).send_keys(new_email)
    driver.find_element(*Input.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Input.INPUT_SECOND_PASSWORD).send_keys(password)

    # Создать аккаунт
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            Registration.CREATE_ACCOUNT_BUTTON
        )
    ).click()

    # Ждем профиль
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h3[@class='profileText name']")
        )
    )

    # Выйти
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[text()='Выйти']")
        )
    ).click()

    # Ждем кнопку входа
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            NavigationLocators.LOGIN_REG_BUTTON
        )
    )

    return {
        "email": new_email,
        "password": password,
    }