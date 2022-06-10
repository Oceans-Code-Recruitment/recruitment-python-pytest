import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # CAN BE USEFUL
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By

service_object = Service(binary_path)

user = {
    'email': 'jose.ig.cabrera.b@gmail.com',
    'password': 'Testing123'
}


@pytest.fixture(autouse=True, scope='function')
def browser():
        driver = webdriver.Chrome(service=service_object)
        driver.maximize_window()
        driver.implicitly_wait(2)
        yield driver
        driver.close()
        driver.quit()

def test_recruitment_example1(browser):
    browser.get("https://app.clickup.com/login")
    browser.find_element(By.CSS_SELECTOR, '#login-email-input').click()
    browser.find_element(By.CSS_SELECTOR, '#login-email-input').send_keys(user['email'])
    browser.find_element(By.CSS_SELECTOR, '#login-password-input').click()
    browser.find_element(By.CSS_SELECTOR, '#login-password-input').send_keys(user['password'])
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    browser.find_element(By.CSS_SELECTOR, '.cu-avatar-container').click() 
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="user-settings-menu"] [class*="column-title-name"]').text == 'Jose Cabrera'
    browser.find_element(By.CSS_SELECTOR, '[data-test*="log-out"]').click()
