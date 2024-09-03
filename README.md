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
   
2. Follow the on-screen menu to interact with the system:

## Functions

- `read_shoes_data(display_message=False)`: Reads and parses shoe data from inventory.txt.
- `capture_shoes()`: Prompts the user to input new shoe details and updates the inventory.
- `view_all()`: Prints out all shoe details and displays a formatted table.
- `re_stock()`: Finds the shoe with the lowest quantity and allows the user to restock it.
- `search_shoe()`: Searches for a shoe by SKU code.
- `value_per_item()`: Calculates and displays the total value of each shoe in inventory.
- `highest_qty()`: Identifies the shoe with the highest quantity and optionally applies a discount.
- `update_file()`: Writes the current inventory data back to inventory.txt.
- `main_menu()`: Displays the main menu and handles user input.

## Notes

- The script expects `inventory.txt` to be present in the same directory. If the file is missing, it will display an error message.
