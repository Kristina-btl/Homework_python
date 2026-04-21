import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop_checkout_total(driver):
         
    wait = WebDriverWait(driver, 20)  

    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Kristina")
    driver.find_element(By.ID, "last-name").send_keys("Bogolyuk")
    driver.find_element(By.ID, "postal-code").send_keys("670047")
    driver.find_element(By.ID, "continue").click()

    total_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_label.text
    assert total_text == "Total: $58.29", (f"Ожидали Total: $58.29, но получили {total_text}")
    driver.quit()
    