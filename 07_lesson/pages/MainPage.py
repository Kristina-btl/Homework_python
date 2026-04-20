from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        # Названия товаров и кнопки добавления
        self.backpack_add = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add = (By.NAME, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
    
    def add_backpack(self):
        self.driver.find_element(*self.backpack_add).click()
    
    def add_bolt_tshirt(self):
        self.driver.find_element(*self.tshirt_add).click()
    
    def add_onesie(self):
        self.driver.find_element(*self.onesie_add).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        