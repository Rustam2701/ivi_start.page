from selene import browser
from selene.core import command


def test_profession_searching():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_sign"]').click()
    browser.element('[type="submit"]').click()