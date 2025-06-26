from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_writer import write_to_excel
from utils.logger import get_logger
from config import config
logger = get_logger("ECOM Price Tracker")

def main():
    logger.info("Starting ECOM Price Tracker...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    driver.implicitly_wait(30)

    try:
        login = LoginPage(driver)
        login.login(config.USERNAME, config.PASSWORD)

        tracker = ProductPage(driver)
        tracker.sort_by_price_desc()
        data = tracker.get_all_products_info()

        write_to_excel(data, config.EXCEL_OUTPUT_PATH)
        logger.info(f"Data saved to {config.EXCEL_OUTPUT_PATH}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()