import allure
from selene import be
from selene.support import by
from selene.support.shared import browser


def test_allure_step(config_browser):
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('/')
    with allure.step('Кликаем а поле поиска'):
        browser.element('.header-search-button').click()
    with allure.step('Вводим в поиск нужную информацию'):
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()
    with allure.step('Кликаем по нужной нам ссылке'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Кликаем на issues'):
        browser.element('#issues-tab').click()
    with allure.step('Проверяем наличие элемента'):
        browser.element(by.partial_text('#81')).should(be.visible)
