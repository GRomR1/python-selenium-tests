from selenium import webdriver

HOST = "localhost"


# get google title with VNC session from Firefox browser
def test_firefox():
    capabilities = {
        "browserName": "firefox",
        "version": "72.0",
        "enableVNC": False,
        "enableVideo": False
    }
    firefox = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                               desired_capabilities=capabilities)
    firefox.get('https://www.google.com')
    print('firefox', firefox.title)
    firefox.quit()


# get google title with VNC session from Chrome browser
def test_chrome():
    capabilities = {
        "browserName": "chrome",
        "version": "80.0_VNC",
        "enableVNC": True,
        "enableVideo": False
    }
    chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                              desired_capabilities=capabilities)
    chrome.get('https://www.google.com')
    print('chrome', chrome.title)
    chrome.quit()


if __name__ == "__main__":
    test_firefox()
    test_chrome()
