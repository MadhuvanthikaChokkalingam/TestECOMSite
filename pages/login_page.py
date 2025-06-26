from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self,driver):
        self.driver= driver
    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message-container").text            