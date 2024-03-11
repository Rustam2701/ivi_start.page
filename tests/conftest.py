import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def browser_config():
    browser.open('https://okko.tv/')
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()
