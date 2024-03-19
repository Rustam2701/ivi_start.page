from selene import browser, have
import allure


@allure.title("Authorization form")
def test_empty_field():
    with allure.step('Open form'):
        browser.element('[aria-label="Consent"]').click()
        browser.element('[test-id=nav_sign]').click()

    with allure.step('Click submit with empty email field'):
        browser.element('[type=submit]').click()
        browser.element('[id="input-phone-error"]').should(have.text('Обязательное поле'))
