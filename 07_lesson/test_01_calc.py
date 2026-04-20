from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalculatorPage import CalculatorPage


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    WebDriverWait(driver, 20)

    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calc = CalculatorPage(driver)

    # 2. Устанавливаем задержку 45 секунд
    calc.set_delay(45)

    # 3. Выполняем вычисление 7 + 8 =
    calc.press_button(calc.button_7)
    calc.press_button(calc.button_plus)
    calc.press_button(calc.button_8)
    calc.press_button(calc.button_equal)

    # 4. Проверка результата
    sleep(50)
    result_text = calc.get_result()
    assert result_text == "15"
    browser.quit()
