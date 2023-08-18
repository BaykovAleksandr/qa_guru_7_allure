import allure
from allure_commons.types import Severity
from selene import be
from selene.support import by
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "BaykovAleksandr")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_search_selene(config_browser):
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#81')).should(be.visible)

