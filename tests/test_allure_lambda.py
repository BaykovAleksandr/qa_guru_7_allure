from selene import be
from selene.support import by
from selene.support.shared import browser
import allure


@allure.step('Открываем шлавную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Ищем нужный нам репозиторий')
def search_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(repo).submit()


@allure.step('Переходим по ссылке {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Кликаем по issues')
def click_issues():
    browser.element('#issues-tab').click()


@allure.step('Кликаем по issues {number}')
def check_number_issues(number):
    browser.element(by.partial_text(number)).should(be.visible)


def test_allure_lambda():
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    click_issues()
    check_number_issues('#81')

