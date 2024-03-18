from selene import browser, have


def test_type_promo():
    browser.open('/')
    browser.element('[test-id="store"]').click()
    browser.element('[class="W6KMKFpE"]').should(have.text('Рекомендации'))
