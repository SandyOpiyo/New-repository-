from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("testuser")
    password.send_keys("password123")

    driver.find_element(By.ID, "login").click()

    assert "dashboard" in driver.current_url

    driver.quit()
