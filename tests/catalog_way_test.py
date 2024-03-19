from selene import browser, have
import allure


@allure.title('Catalog must have text "series"')
def test_catalog_way():
    with allure.step('Open catalog'):
        browser.open('/')
        browser.element('[test-id=web_main]').click()

    with allure.step('Go to series'):
        browser.element('[alt=Сериалы]').click()
        browser.element('[class=tKhgprU3]').should(have.text('Сериалы'))

