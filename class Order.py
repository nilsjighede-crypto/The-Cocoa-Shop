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