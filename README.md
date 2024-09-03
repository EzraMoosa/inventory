# Shoe Inventory Management System

## Overview

The Shoe Inventory Management System is a simple Python application designed to manage and maintain an inventory of shoes. It allows users to read shoe data from a file, capture new shoe entries, view all shoes, restock items, search for specific shoes, calculate the value per item, and check the shoe with the highest quantity. The system utilizes a text file (`inventory.txt`) for data storage and presents information using the `tabulate` library for formatted tables.

## Features

- **Read Shoes Data**: Load shoe data from `inventory.txt`, skipping the headers.
- **Capture New Shoes**: Add new shoe entries to the inventory.
- **View All Shoes**: Display all shoes in inventory with their details.
- **Re-stock Shoes**: Identify and restock the shoe with the lowest quantity.
- **Search For A Shoe**: Find a shoe by its SKU code.
- **Calculate Value Per Item**: Display the total value of each shoe in stock.
- **Check Product With Highest Quantity**: Find and optionally apply a discount to the shoe with the highest quantity.

## Installation

1. Ensure you have Python 3 installed.
2. Install the `tabulate` library using pip:
   `pip install tabulate`

## Usage

Run the following command:
1. `python inventory.py`
   
3. Follow the on-screen menu to interact with the system:

- **1 - Read Shoes Data**
- **2 - Capture New Shoes**
- **3 - View All Shoes**
- **4 - Re-stock Shoes**
- **5 - Search For A Shoe**
- **6 - Calculate Value Per Item**
- **7 - Check Product With Highest Quantity**
- **8 - Exit**

## Notes

- The script expects `inventory.txt` to be present in the same directory. If the file is missing, it will display an error message.
