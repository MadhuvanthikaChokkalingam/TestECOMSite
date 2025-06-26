# TestECOMSite - E-Commerce Price Tracker

A Python-based Selenium automation framework that logs into [SauceDemo](https://www.saucedemo.com/), sorts products by price (high to low), extracts product information, and writes it to an Excel file. The framework also includes automated test cases using `pytest`.


## Features and funtional requirements

- Automates login to SauceDemo (valid & invalid credentials)
- Sorts products by **"Price (high to low)"**
- Extracts:
  - Product Name
  - Product Price
  - Product Description
- Stores data in an Excel file with timestamp
- Includes test cases using `pytest`
- Logging support for better debugging

### Setup instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/TestECOMSite.git cd TestECOMSite

2. Install dependencies
   pip install -r requirements.txt

3. Run the Project
```bash
python main.py


The script will:
- Open Chrome
- Log in
- Sort products
- Extract data
- Save data to data/products_output.xlsx

