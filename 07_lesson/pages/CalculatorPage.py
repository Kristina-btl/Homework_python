from selenium.webdriver.common.by import By 

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CLASS_NAME, "screen")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equal = (By.XPATH, "//span[text()='=']")

    def set_delay(self, seconds):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(seconds))
    
    def press_button(self, button_locator):
        self.driver.find_element(*button_locator).click()
    
    def get_result(self):
        return self.driver.find_element(*self.result_field).text