from selene import browser, have


def test_start_page_auth():
    browser.open('/')
    browser.element('[test-id=nav_sign]').click()
    browser.element('[type=submit]').click()
    browser.element('[id="input-phone-error"]').should(have.text('Обязательное поле'))
