from selene import browser, have
import allure


@allure.title('Authorization invalid email')
def test_invalid_email():
    with allure.step('Open form'):
        browser.open('/')
        browser.element('[test-id=nav_sign]').click()

    with allure.step('Type invalid email'):
        browser.element('[inputmode="text"]').type('asdfgsbfvsgmail.com')
        browser.element('[type=submit]').click()

    with allure.step('Check of system answer'):
        browser.element('[id="input-phone-error"]').should(have.text('Неверный формат e-mail'))

