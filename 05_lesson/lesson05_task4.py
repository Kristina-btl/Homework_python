from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")

username_field.send_keys("tomsmith")

sleep (5)

password_field = driver.find_element(By.ID, "password")

password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

sleep (5)

message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print(message.text)


driver.quit()