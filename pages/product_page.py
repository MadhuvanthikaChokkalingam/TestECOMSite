from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_by_price_desc(self):
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_visible_text("Price (high to low)")

    def get_all_products_info(self):
        results = []
        product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for product in product_elements:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            desc = product.find_element(By.CLASS_NAME, "inventory_item_desc").text
            results.append({
                "Product Name": name,
                "Product Price": price,
                "Product Description": desc
            })
        return results
