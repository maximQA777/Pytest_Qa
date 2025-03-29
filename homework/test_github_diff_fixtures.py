from selene import browser, by


def test_desktop(desktop_resolution):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


def test_mobile(mobile_resolution):
    browser.open("http://github.com")
    browser.element('.Button-content').click()
    browser.element(by.text("Sign up")).click()