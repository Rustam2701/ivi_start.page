import pytest
from selene import browser, be
import allure


@pytest.fixture(params=[(896, 414)], scope='function')
def mobile_browser(request):
    browser.config.base_url = 'https://okko.tv'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@allure.title('Check mobile size page')
def test_mobile_clickable_burger(mobile_browser):
    with allure.step('Burger most be clickable, visible'):
        browser.open('/')
        browser.element('[aria-label="Consent"]').click()
        browser.element('[test-id=nav_menu]').click()
        browser.element('[test-id=mnav_mainsport]').should(be.visible).press_enter()
