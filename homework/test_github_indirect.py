import pytest
from selene import browser, by


@pytest.mark.parametrize("desktop_resolution", [(1650, 1050)], indirect=True)
def test_desktop(desktop_resolution):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


@pytest.mark.parametrize("mobile_resolution", [(900, 1000)], indirect=True)
def test_mobile(mobile_resolution):
    browser.open("http://github.com")
    browser.element('.Button-content').click()
    browser.element(by.text("Sign up")).click()