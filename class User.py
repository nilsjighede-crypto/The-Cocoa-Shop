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