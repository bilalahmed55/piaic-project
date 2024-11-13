# Inventory Management System (IMS)
import getpass

# ----------------------------
# Product Class (OOP Concepts)
# ----------------------------
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        """Adjust stock quantity by a specified amount."""
        self.stock_quantity += quantity
        print(f"Stock updated for {self.name}. New stock: {self.stock_quantity}")

    def __str__(self):
        return f"{self.product_id} - {self.name} | Category: {self.category} | Price: ${self.price} | Stock: {self.stock_quantity}"

# ----------------------------
# Inventory Class (CRUD Operations)
# ----------------------------
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """Add a new product to the inventory."""
        self.products[product.product_id] = product
        print(f"Product '{product.name}' added.")

    def edit_product(self, product_id, **kwargs):
        """Edit product details."""
        product = self.products.get(product_id)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            print(f"Product '{product_id}' updated.")
        else:
            print(f"Product with ID {product_id} not found.")

    def delete_product(self, product_id):
        """Remove a product from the inventory."""
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' deleted.")
        else:
            print(f"Product with ID {product_id} not found.")

    def view_products(self):
        """Display all products."""
        for product in self.products.values():
            print(product)

    def search_product(self, search_term):
        """Search for products by name or category."""
        results = [p for p in self.products.values() if search_term.lower() in p.name.lower() or search_term.lower() in p.category.lower()]
        if results:
            for product in results:
                print(product)
        else:
            print(f"No products found for '{search_term}'.")

    def filter_by_stock(self, threshold):
        """Filter products based on stock levels."""
        low_stock_products = [p for p in self.products.values() if p.stock_quantity <= threshold]
        if low_stock_products:
            for product in low_stock_products:
                print(product)
        else:
            print("All products have sufficient stock.")

# ----------------------------
# Authentication and Role Management
# ----------------------------
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class AuthSystem:
    def __init__(self):
        self.users = {"admin": User("admin", "Admin"), "user": User("user", "User")}
    
    def login(self):
        """Basic login with username and password validation."""
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        # Password validation can be added here
        user = self.users.get(username)
        if user and password == "password":  # Using a fixed password for simplicity
            print(f"Welcome, {username}!")
            return user
        else:
            print("Invalid login.")
            return None

# ----------------------------
# Main Application
# ----------------------------
class InventoryManagementSystem:
    def __init__(self):
        self.inventory = Inventory()  # Persistent inventory instance
        self.auth_system = AuthSystem()
    
    def start(self):
        while True:
            user = self.auth_system.login()
            if not user:
                print("Login failed. Try again.")
                continue
            
            while True:
                print("\nOptions:")
                print("1. View Products")
                print("2. Search Products")
                print("3. Filter by Stock")
                
                if user.role == "Admin":
                    print("4. Add Product")
                    print("5. Edit Product")
                    print("6. Delete Product")
                
                print("0. Logout")
                print("Q. Quit")  # Quit option to stop the program
                choice = input("Enter option: ")
                
                if choice == "1":
                    self.inventory.view_products()
                elif choice == "2":
                    search_term = input("Enter product name or category to search: ")
                    self.inventory.search_product(search_term)
                elif choice == "3":
                    threshold = int(input("Enter stock level threshold: "))
                    self.inventory.filter_by_stock(threshold)
                elif choice == "4" and user.role == "Admin":
                    product_id = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    category = input("Enter Product Category: ")
                    price = float(input("Enter Product Price: "))
                    stock_quantity = int(input("Enter Stock Quantity: "))
                    product = Product(product_id, name, category, price, stock_quantity)
                    self.inventory.add_product(product)
                elif choice == "5" and user.role == "Admin":
                    product_id = input("Enter Product ID to edit: ")
                    field = input("Enter field to edit (name, category, price, stock_quantity): ")
                    value = input("Enter new value: ")
                    if field in {"price", "stock_quantity"}:
                        value = float(value) if field == "price" else int(value)
                    self.inventory.edit_product(product_id, **{field: value})
                elif choice == "6" and user.role == "Admin":
                    product_id = input("Enter Product ID to delete: ")
                    self.inventory.delete_product(product_id)
                elif choice == "0":
                    print("Logging out.")
                    break
                elif choice.upper() == "Q":
                    print("Exiting the program.")
                    return  # Exit the start method to terminate the program
                else:
                    print("Invalid option. Please try again.")

# ----------------------------
# Run the IMS
# ----------------------------
if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.start()
