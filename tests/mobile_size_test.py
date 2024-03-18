import pytest
from selene import browser, be


@pytest.fixture(params=[(896, 414)])
def mobile_browser(request):
    browser.config.base_url = 'https://okko.tv'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


def test_mobile_menu(mobile_browser):
    browser.open('/')
    browser.element('[test-id=nav_menu]').click()
    browser.element('[test-id=mnav_mainsport]').should(be.visible).press_enter()
