# Reference:
# https://www.quora.com/How-do-you-skip-the-first-line-of-a-text-file-in-Python
# https://pypi.org/project/tabulate/
# https://www.askpython.com/python-modules/tabulate-tables-in-python
# https://medium.com/@johnidouglasmarangon/padding-f-strings-in-python-977b17edbd36


import sys
from tabulate import tabulate


class Shoe:
    """Class for Shoe object.
    
    Keyword arguments:
        - Country  (str)   : The country in which the stocks are located
        - Code     (str)   : The code/ SKU of the shoe
        - Product  (str)   : Product name or model
        - Cost     (float) : The cost of the shoe
        - Quantity (int)   : The quantity of shoes in stock
    """

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):

        """Return the cost of the shoes."""

        return float(self.cost)
        

    def get_quantity(self):

        """Return the quantity of the shoes."""

        return int(self.quantity)


    def __str__(self):

        """Return a string representation of the shoe."""

        return \
f"""The Nike {self.product} 

Costs   :R{float(self.cost):.2f} Retail
Country :{self.country}
Stock   :{self.quantity} unit(s) in-stock.
SKU     :{self.code}"""

# Initialize empty shoe list
shoe_list = []


def read_shoes_data(display_message=False):

    """Get all the data from inventory file and append to list."""

    # Clear list so objects are not added twice
    shoe_list.clear()

    # Validate file exists
    try:
        with open("inventory.txt", "r") as file:
            data = file.readlines()[1:]

        # Separate and store all values
        for index, line in enumerate(data):
            try:    
                line = line.strip().split(",")
                country = line[0]
                code = line[1]
                product = line[2]
                cost = line[3]
                quantity = line[4]

                # Create shoe object and append to shoe_list
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

            except ValueError:
                print(f"Error in line {index + 1}: Invalid data format.")
                continue
        if display_message:
            print("\n--- Shoes has been read successfully. ---")

    except FileNotFoundError as e:
        print(f"--- {e} does not exist. ---")
    

def capture_shoes():

    """Capture new shoes and add it to list."""

    while True:
        # Get shoe attributes from user and validate their inputs
        country = input(
            "\nWhich country is the shoes stored at: ").title()
        if not country.strip(): 
            print("\n--- Input cannot be blank. Try again. ---")
            continue
            
        code = input("What is the code of the shoe (eg. 12345): ")
        if not code.strip():
            print("\n--- Input cannot be blank. Try again. ---")
            continue
        if not code.isdigit():
            print("\n--- Input must have numeric value. ---")
            continue
        code = "SKU" + code 

        # Check all user inputs for blank inputs or data
        product = input("What is the name of the shoe: ")
        if not product.strip():
            print("\n--- Input cannot be blank. Try again. ---")
            continue

        cost = input("What is the cost of the shoe: R")
        if not cost.strip():
            print("\n--- Input cannot be blank. Try again. ---")
            continue
        if not cost.isdigit():
            print("\n--- Input must have numeric value. ---")
            continue
        cost = round(float(cost))

        quantity = input("How much shoes are there: ")
        if not quantity.strip():
            print("\n--- Input cannot be blank. Try again. ---")
            continue  
        if not quantity.isdigit():
            print("\n--- Input must have numeric value. ---")
            continue
        quantity = int(quantity)

        # Create and append Shoe object to list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        update_file()

        print("\n--- New shoe added to inventory. ---")
        break
        

def view_all():

    """Prints out all shoes with attributes in table format."""

    print("")

    for shoe in shoe_list:
        print("")
        print(shoe.__str__())

    print("")
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data = [[shoe.country, shoe.code, shoe.product, \
                  f"R{float(shoe.cost):.2f}", shoe.quantity] \
                    for shoe in shoe_list]
    print(tabulate(shoe_data, headers=headers))


def re_stock():

    """Checks for shoe with the lowest quantity and allows user to re-stock."""

    # Validate that the shoe list is not empty
    if not shoe_list:
        print("--- No shoes available for restocking. ---")
        return
    
    lowest_quantity_shoe = shoe_list[0]
    # Check for any shoe quantity lower than one above
    for shoe in shoe_list[1:]:
        if int(shoe.quantity) < int(lowest_quantity_shoe.quantity):
            lowest_quantity_shoe = shoe

    # Display shoe with lowest quantity
    print(f"\nLowest quantity:\n----------------\n{lowest_quantity_shoe}.")
    
    restock_choice = input(
        "\nDo you want to restock this shoe? (Y / N): ").lower()

    # Confirmation of shoe re-stocking
    if restock_choice == "y" or restock_choice == "yes":
        restock_quantity = int(input(
            "Enter the amount of shoes you would like to add: "))
        
        # Add restock quantity to shoe quantity
        lowest_quantity_shoe.quantity = str(
            int(lowest_quantity_shoe.quantity) + restock_quantity)
        print(f"\n--- {restock_quantity} shoe(s) has been added to your" + \
              f" inventory. --")
        
        update_file()

    elif restock_choice == "n" or restock_choice == "no":
        print("\n--- No shoes have been restocked. ---")
    
    else:
        print("\n--- Invalid choice. ---")


def search_shoe():

    """Search for a shoe using a code/ (SKU)."""

    # Get SKU from user
    search_code = "SKU" + \
        input("Enter the code/ SKU you would like to search: ")

    # Comparison to find if SKU exists
    for shoe in shoe_list:
        if shoe.code == search_code:
            return shoe
        
    return None


def value_per_item():

    """Prints out the total value of each shoe."""

    print("\nValue per item:\n---------------")

    # Print out the value of every shoe. (value = cost * quantity)
    for shoe in shoe_list:

        cost = shoe.get_cost()
        quantity = shoe.get_quantity()
        value = cost * quantity

        print(f"{shoe.product:<20} : R{value:.2f}")


def highest_qty():

    """Check for the shoe with the highest quantity."""

    # Validate that the shoe list is not empty
    if not shoe_list:
        print("\n--- No shoes available for restocking. ---")
        return
    
    highest_quantity_shoe = shoe_list[0]
    # Check for quantity higher than one above
    for shoe in shoe_list:
        if int(shoe.quantity) > int(highest_quantity_shoe.quantity):
            highest_quantity_shoe = shoe
    print(f"\nHighest quantity shoe:\n----------------------")
    print(f"{highest_quantity_shoe.product} with " + \
          f"{highest_quantity_shoe.quantity} unit(s) left.")
    print("-------------------------------------------------")
    
    # Ask user for discount percentage and display sale price for shoe
    try:
        discount_percentage = float(input(
            "Enter the percentage of discount you want to apply (eg. 20): "))

        discount_price = \
            float(highest_quantity_shoe.cost) * \
                  (1 - (discount_percentage / 100))
        previous_cost = highest_quantity_shoe.cost

        # Set new price
        highest_quantity_shoe.cost = round(discount_price)
        print(f"""\n{highest_quantity_shoe.product} is now on sale!
Sale price: R{round(float(discount_price))}
Old price:  R{round(float(previous_cost))}""")

        update_file()

    except ValueError:
        print("\n --- Invalid input. Try again. ---")
        highest_qty()


def update_file():

    """Update the contents of the external 'inventory.txt' file."""

    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost}," + 
                    f"{shoe.quantity}\n")
                
    except (FileNotFoundError, PermissionError) as e:
        print(f"--- {e} does not exist. ---")


def main_menu():
    print("\n---------------- Shoe Inventory Management v0.1 ----------------")
    print(f"""
1 - Read Shoes Data
2 - Capture New Shoes
3 - View All Shoes
4 - Re-stock Shoes
5 - Search For A Shoe
6 - Calculate Value Per Item
7 - Check Product With Highest Quantity
8 - Exit
""")
    choice = input("Enter a number between (1 - 8) : ")
    return choice


if __name__ == "__main__":
    
    # Initialize data before user selects menu options
    read_shoes_data(False)

    while True:
        choice = main_menu()

        if choice == "1":
            read_shoes_data(True)

        elif choice == "2":
            capture_shoes()

        elif choice == "3":
            view_all()

        elif choice == "4":
            re_stock()

        elif choice == "5":
            shoe = search_shoe()

            if shoe:
                print(f"\nShoe found:\n-----------\n{shoe}")
            else:
                print("\n--- Shoe NOT found. ---")

        elif choice == "6":
            value_per_item()

        elif choice == "7":
            highest_qty()

        elif choice == "8":
            print("\n--- Exiting application. Goodbye! ---\n")
            sys.exit()

        else:
            print("\n--- Invalid selection. Enter a number between (1 - 8). ---")
            