import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", 
                 help="Choose language: ")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_experimental_option('prefs', {'intl.accept_languages' : user_language})
        print("\nstart chrome browser for test...")
        browser = webdriver.Chrome("chromedriver", options = options)
    elif browser_name == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test...")
        browser = webdriver.Firefox(firefox_profile = firefox_profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")    
    yield browser
    print("\nquit browser...")
    browser.quit()

    

