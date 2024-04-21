import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoketest
@allure.title("Verify the IDrive360 website login page")
@allure.description("Simple login TC of IDrive360 webpage")
def test_login_idrive():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(5)
    username = driver.find_element(By.NAME,value="username")
    username.send_keys("augtest_040823@idrive.com")
    time.sleep(5)
    password = driver.find_element(By.NAME,value="password")
    password.send_keys("123456")
    time.sleep(5)
    submit_btn = driver.find_element(By.ID,value="frm-btn")
    submit_btn.click()
    time.sleep(20)
    allure.attach(driver.get_screenshot_as_png(),name="login-screenshot", attachment_type=AttachmentType.PNG)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    driver.quit()