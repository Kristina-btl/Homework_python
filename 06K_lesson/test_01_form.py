import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.quit()

def test_form_submission_color_highlighting(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.NAME, "job-position").send_keys("QA")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class"),"Zip code не подсвечен красным"

# Проверяем остальные поля
    green_fields = {"firstName": "Иван",
            "lastName": "Петров",
            "address": "Ленина, 55-3",
            "email": "test@skypro.com",
            "phoneNumber": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job": "QA",
            "company": "SkyPro"}

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым"

    driver.quit()
