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