from selene import browser, have


def test_catalog_way():
    browser.open('/')
    browser.element('[test-id="web_main"]').click()
    browser.element('[alt="Сериалы"]').click()
    browser.element('[class="tKhgprU3"]').should(have.text('Сериалы'))

