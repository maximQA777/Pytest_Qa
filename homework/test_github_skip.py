import pytest
from selene import browser, query


def test_mobile_skip( setup_browser):
    if  setup_browser == "mobile":
        pytest.skip("Это мобильное разрешение")
    browser.open('https://github.com/')
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))


def test_desktop_skip(setup_browser):
    if  setup_browser == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open('https://github.com/')
    browser.element('.Button-content').click()
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))