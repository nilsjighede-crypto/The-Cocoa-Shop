tax = 0.8

class MainSystem:
    def __init__(self, first_last_name, email, password):
        self.first_last_name = first_last_name
        self.email = email
        self.password = password

    def login(self):
        self.first_last_name = input("Enter first and last name: ")
        while True:
            self.email = input("Enter email: ")

            if "@" in self.email:
                break
            else: 
                print(f"Invalid email, try again") 
        
        self.password = input("Enter password: ")
        print("Successfully logged in!")
        
        

    def get_details(self):
        return f"Logged in to {self.email}'s account"

    def logout():
        return f"You have been logged out!"

    def create_order():
        return f"Order created!"

    def add_or_remove_item_to_order():
        order = input("Type 'add' to add an item or 'remove' to remove an item:\n")
        if order == "add".lower():
            print("Item added")
        elif order == "remove".lower():
            print("Item removed")
        else:
            print("Error, type add or remove")

    def checkout_order():
        checkout_order = input("Do you want to checkout order? Yes/no")
        if checkout_order == "yes".lower():
            print("Order confirmed! ")
        elif checkout_order == "no".lower():
            print("Continue browsing")
        else:
            print("Error, type yes or no")
        
class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
    
    def check_password(self):
        pass

class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id

class Wholesale(Customer):
    def __init__(self, name, email, customer_id, discount_rate ):
        super().__init__(name, email, customer_id)
        self.discount_rate = discount_rate

class Staff(User):
    def __init__(self, name, email, staff_id, password):
        super().__init__(name, email) 
        self.staff_id = staff_id 
        self.password = password

class Order:
    def __init__(self, order_id, order_date, customer, order_location, order_lines, order_creator):
        self.order_id = order_id
        self.order_date = order_date
        self.customer = customer
        self.order_location = order_location
        self.order_lines = order_lines
        self.order_creator = order_creator
  
    def add_item(self):
        pass
    def decrease_item(self):
        pass
    def remove_item(self):
        pass
    def calculate_total(self):
        pass


class OrderLine:
    def __init__(self, product, product_qty):
        self.product = product
        self.product_qty = product_qty
    
    def increase_qty(self):
        pass
    def decrease_qty(self):
        pass
    def total_line(self):
        pass

class Prodcuct:
    def __init__(self, product_id, product_name, product_price, product_cost, wholsale_avalible, product_category, shelf_life_days):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_cost = product_cost
        self.wholsale_avalible = wholsale_avalible
        self.product_category = product_category
        self.shelf_life_days = shelf_life_days
    
    def calculate_profit(self):
        pass
    def get_product_info(self):
        pass
    def check_shelf_life(self):
        pass

class Inventory:
    def __init__(self, inventory_id, location, stock):
        self.inventory_id = inventory_id
        self.location = location
        self.stock = stock
    def withdraw_stock(self):
        pass
    def add_stock(stock):
        pass

class Shipment:
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
        
    def get_tracking_info(self):
        pass


staff1 = MainSystem("", "", "")
staff1.login()
print(staff1.get_details())
print()

choose_action = input("Choose action:\nAdd/remove item = 1\nLogout == 2\nAction: ")
if choose_action == "1":
    print(MainSystem.add_or_remove_item_to_order())
elif choose_action == "2":
    print(MainSystem.logout())
else:
    print("Type 1 or 2")

        











