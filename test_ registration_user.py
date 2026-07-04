
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import NavigationLocators, Autorization, Registration, Input
def test_successful_registration(driver):
  random_number = random.randint(100,999)
  domains = ["gmail.com", "yandex.ru", "mail.ru", "rambler.ru"]
  random_domains = random.choice(domains)
  new_email = f'user{random_number}@{random_domains}'

  

  expected_result_username = 'User.'



#кнопка "Вход/регистрация"
  driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

#ожидание пока появится кнопка
  WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(Autorization.NOT_ACCOUNT_BUTTON))


#кнопка "Нет аккаунта"
  driver.find_element(*Autorization.NOT_ACCOUNT_BUTTON).click()

#ввод эмейла
  driver.find_element(*Input.INPUT_EMAIL).send_keys(new_email)
#ввод пароля
  driver.find_element(*Input.INPUT_PASSWORD).send_keys('123456')
#ввод повторно пароля
  driver.find_element(*Input.INPUT_SECOND_PASSWORD).send_keys('123456')


#нажать ккнопку "Создать аккаунт"
  WebDriverWait(driver, 5).until(
    expected_conditions.element_to_be_clickable(Registration.CREATE_ACCOUNT_BUTTON)
).click()
#ожидаем прогрузки страницы
  WebDriverWait(driver, 5).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//h3[@class='profileText name']"))
)
#сравниваем ОР и ФР
  actual_result_username = driver.find_element(By.XPATH, "//h3[contains(@class, 'profileText')]").text
  assert actual_result_username == expected_result_username


  avatar_content = driver.find_element(By.CSS_SELECTOR, "div.flexRow button svg")

# Проверяем, что иконка отображается на экране
  assert avatar_content.is_displayed(), "Дефолтный аватар (тег <svg>) не отображается!"

 