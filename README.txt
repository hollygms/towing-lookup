# VIN Towing Capacity Lookup Tool #

This project validates vehicle VINs using an external API.  
Invalid VINs will be marked with "VIN ERROR" in the CSV.

Valid VINs for **Ford vehicles** within the model years **2020–2025** will be submitted to the official Ford VIN lookup site using Selenium and ChromeDriver.

The CSV will then be updated with:
- The vehicle’s maximum towing capacity
- The source URL used for reference

## How to Use ##

1. Place your CSV file in the same folder as the `.py` files.
2. Run `main.py`.
3. When prompted, enter the **exact name** of your CSV file.
4. The file will be updated in-place with the new towing capacity data.

