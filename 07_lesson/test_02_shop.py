import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait

def test_saucedemo_shopping():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    WebDriverWait(driver, 20)

        # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")

        # 2. Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
        # После входа страницы автоматически загружаются

        # 3. Добавление товаров
    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_bolt_tshirt()
    main_page.add_onesie()
    main_page.go_to_cart()

        # 4. Перейти в корзину и оформить заказ
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Петров", "12345")
    total_text = checkout_page.get_total()

        # 5. Проверка итоговой суммы
        # Ожидаем "$58.29"
    assert total_text == "Total: $58.29", (
                f"Ожидали Total: $58.29, но получили {total_text}")

    driver.quit()
