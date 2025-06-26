import os
from openpyxl import Workbook
from datetime import datetime

def write_to_excel(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Products"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ws.append([f"Generated On: {timestamp}"])
    ws.append([])  

    headers = ["Product Name", "Product Price", "Product Description"]
    ws.append(headers)

    for row in data:
        ws.append([row["Product Name"], row["Product Price"], row["Product Description"]])

    wb.save(filename)
