import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_writer import write_to_excel
import config.config as config

@pytest.fixture(scope="function")
def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_price_extraction(setup_driver):
    login = LoginPage(setup_driver)
    login.login(config.USERNAME, config.PASSWORD)

    page = ProductPage(setup_driver)
    page.sort_by_price_desc()
    time.sleep(10)
    data = page.get_all_products_info()
    assert "inventory" in setup_driver.current_url
    WebDriverWait(setup_driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    time.sleep(10)
    assert len(data) > 0
    write_to_excel(data, config.EXCEL_OUTPUT_PATH)

def test_invalid_login(setup_driver):
    login = LoginPage(setup_driver)
    login.login(config.USERNAME, config.INVALID_PASSWORD)
    error_msg = login.get_error_message()
    assert error_msg.__contains__("Epic sadface")