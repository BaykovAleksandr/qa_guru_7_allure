import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.config.base_url = 'https://github.com'
    driver.set_window_size(1920, 1080)
    yield
    browser.quit()

