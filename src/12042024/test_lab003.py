from selenium import webdriver

# Selenium 4


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    # Python Inte -> optimize if there s not command, I will stop the execution.