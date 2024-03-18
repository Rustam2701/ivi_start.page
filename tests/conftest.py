import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def browser_config():
    browser.config.base_url = 'https://okko.tv'
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield

    browser.quit()
