from selene import browser, have
import allure


@allure.title('In shop must be recommendations')
def test_recommendations_in_shop():
    with allure.step('Open shop page'):
        browser.open('/')
        browser.element('[test-id="store"]').click()

    with allure.step('Check text "recommendations"'):
        browser.element('[class="W6KMKFpE"]').should(have.text('Рекомендации'))
