import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")

def Login_Logout_Setup():
    driver = webdriver.Chrome(executable_path=r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver

    time.sleep(5)
    driver.find_element_by_xpath("//p[@class='oxd-userdropdown-name']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[normalize-space()='Logout']").click()
    driver.close()
