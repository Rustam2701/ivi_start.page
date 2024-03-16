from selene import browser


def test_start_page_auth():
    browser.open('/')
    browser.element('[test-id="nav_sign"]').click()
    browser.element('[type="submit"]').click()
