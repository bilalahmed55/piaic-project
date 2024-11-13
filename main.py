# Inventory Management System with Classes, Error Handling, and Quit Option

# Sample data for users
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Sample product data as class
class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Category: {self.category} | Price: {self.price} | Stock: {self.stock}"

# Inventory class to manage products
class Inventory:
    def __init__(self):
        self.products = [
            Product(1, 'Product 1', 'Category A', 100, 50),
            Product(2, 'Product 2', 'Category B', 150, 30)
        ]
    
    def view_products(self):
        print("\nAll Products:")
        if not self.products:
            print("No products in the inventory.\n")
        for product in self.products:
            print(product)
        print()

    def search_product(self, search_term):
        found = False
        search_term = search_term.lower()
        for product in self.products:
            if search_term in product.name.lower() or search_term in product.category.lower():
                print(f"Found: {product}")
                found = True
        if not found:
            print("No products found.\n")
    
    def add_product(self, name, category, price, stock):
        new_product = Product(len(self.products) + 1, name, category, price, stock)
        self.products.append(new_product)
        print(f"Product {name} added successfully!\n")

    def edit_product(self, product_id, name, category, price, stock):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            product.name = name
            product.category = category
            product.price = price
            product.stock = stock
            print(f"Product {product_id} updated successfully!\n")
        else:
            print("Product not found.\n")

    def delete_product(self, product_id):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            self.products.remove(product)
            print(f"Product {product_id} deleted successfully!\n")
        else:
            print("Product not found.\n")


# Main application class to handle login and menus
class InventoryManagementSystem:
    def __init__(self):
        self.users = {
            'admin': 'password',
            'user': 'password'
        }
        self.inventory = Inventory()

    def login(self):
        print("Welcome to the Inventory Management System!")
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if username in self.users and self.users[username] == password:
                print(f"Welcome, {username}!")
                return username
            else:
                print("Invalid username or password! Please try again.\n")

    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. View Products")
            print("2. Search Products")
            print("0. Logout")
            print("Q. Quit Application")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                self.inventory.view_products()
            elif choice == '2':
                search_term = input("Enter product name or category to search: ")
                self.inventory.search_product(search_term)
            elif choice == '0':
                print("Logging out...\n")
                break
            elif choice.lower() == 'q':
                print("Quitting the application...\n")
                exit(0)  # Exit the program
            else:
                print("Invalid option, please select a valid menu option.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View Products")
            print("2. Search Products")
            print("3. Add Product")
            print("4. Edit Product")
            print("5. Delete Product")
            print("0. Logout")
            print("Q. Quit Application")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                self.inventory.view_products()
            elif choice == '2':
                search_term = input("Enter product name or category to search: ")
                self.inventory.search_product(search_term)
            elif choice == '3':
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = self.get_valid_price()
                stock = self.get_valid_stock()
                self.inventory.add_product(name, category, price, stock)
            elif choice == '4':
                product_id = self.get_valid_product_id()
                name = input("Enter new name: ")
                category = input("Enter new category: ")
                price = self.get_valid_price()
                stock = self.get_valid_stock()
                self.inventory.edit_product(product_id, name, category, price, stock)
            elif choice == '5':
                product_id = self.get_valid_product_id()
                self.inventory.delete_product(product_id)
            elif choice == '0':
                print("Logging out...\n")
                break
            elif choice.lower() == 'q':
                print("Quitting the application...\n")
                exit(0)  # Exit the program
            else:
                print("Invalid option, please select a valid menu option.")

    def get_valid_price(self):
        while True:
            try:
                price = float(input("Enter product price: "))
                if price <= 0:
                    print("Price must be a positive number. Please try again.")
                else:
                    return price
            except ValueError:
                print("Invalid input! Please enter a valid number for the price.")

    def get_valid_stock(self):
        while True:
            try:
                stock = int(input("Enter product stock quantity: "))
                if stock < 0:
                    print("Stock quantity cannot be negative. Please try again.")
                else:
                    return stock
            except ValueError:
                print("Invalid input! Please enter a valid number for the stock.")

    def get_valid_product_id(self):
        while True:
            try:
                product_id = int(input("Enter product ID: "))
                if product_id <= 0:
                    print("Product ID must be a positive number. Please try again.")
                return product_id
            except ValueError:
                print("Invalid input! Please enter a valid product ID.")

    def run(self):
        while True:
            user = self.login()
            
            if user:
                if user == 'admin':
                    self.admin_menu()
                elif user == 'user':
                    self.user_menu()
            else:
                print("Please try logging in again.\n")


if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.run()
