from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import NavigationLocators, Autorization, Input, Advert, ProfilePage


def test_create_advert_auth_user(driver, create_user):
    advert_name = "name"
    wait = WebDriverWait(driver, 5)

    # Авторизация
    driver.find_element(*NavigationLocators.LOGIN_REG_BUTTON).click()

    # Ввод email (ждем его появления)
    wait.until(EC.visibility_of_element_located(Input.INPUT_EMAIL)).send_keys(create_user["email"])
    
    # Пароль и логин вводим через find_element, как у тебя и работало
    driver.find_element(*Input.INPUT_PASSWORD).send_keys(create_user["password"])
    driver.find_element(*Autorization.LOGIN_BUTTON).click()

    # Ждем кнопку профиля (значит, вошли)
    wait.until(EC.visibility_of_element_located(NavigationLocators.PROFIL_BUTTON))

    # Переход к созданию
    wait.until(EC.element_to_be_clickable(NavigationLocators.CREATE_ADVERT)).click()
    wait.until(EC.visibility_of_element_located(Advert.INPUT_NAME)).send_keys(advert_name)

    # Оптимизировано: убрали дублирующий driver.find_element для описания и цены
    wait.until(EC.presence_of_element_located(Advert.INPUT_DESCRIPTION)).send_keys("description")
    wait.until(EC.presence_of_element_located(Advert.INPUT_PRICE)).send_keys("123")

    # Город и категория (клики по селектам)
    wait.until(EC.visibility_of_element_located(Advert.DROPDOWN_CITY_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(Advert.DROPDOWN_CITY_SELECT)).click()
    
    wait.until(EC.element_to_be_clickable(Advert.DROPDOWN_CATEGORY_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(Advert.DROPDOWN_CATEGORY_SELECT)).click()

    # Радио-кнопка и публикация через find_element (они уже есть на экране)
    driver.find_element(*Advert.RADIO_USED).click()
    driver.find_element(*Advert.PUBLISH_BUTTON).click()

    # Переход в профиль
    wait.until(EC.element_to_be_clickable(NavigationLocators.PROFIL_BUTTON)).click()
    
    # Возвращаем проверку страницы профиля, чтобы гарантировать переход
    wait.until(EC.visibility_of_element_located(ProfilePage.MY_ADVERTS))

    # Собираем имена объявлений
    adverts = wait.until(EC.visibility_of_any_elements_located(ProfilePage.ALL_ADVERTS_NAMES))
    advert_names = [advert.text for advert in adverts]

    assert advert_name in advert_names
