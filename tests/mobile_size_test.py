import pytest
from selene import browser


@pytest.fixture(params=[(896, 414)])
def mobile_browser(request):
    browser.config.base_url = 'https://okko.tv'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height


def test_mobile_menu(mobile_browser):
    browser.open('/')
    browser.element('[test-id="nav_menu"]').click()
