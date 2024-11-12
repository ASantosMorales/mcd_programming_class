# ******* Classes definition ************
class product:
    def __init__(self, regular_price, inventory, discount_percentage):
        self.regular_price = regular_price 
        self.inventory = inventory
        self.discount_percentage = discount_percentage
        self.price_with_discount = round(self.regular_price - (self.discount_percentage/100 * self.regular_price), 2)
        self.discount_amount = round(self.regular_price - self.price_with_discount, 2)

    def purchasing(self, purchased_quantity):
        self.inventory -= purchased_quantity

class customer:
    def __init__(self, customer_id, entered_name, user_shopping_cart):
        self.customer_id = customer_id
        self.entered_name = entered_name
        self.cart = user_shopping_cart
        self.is_active = False
        self.history = []

    def cart_deletion(self):
        self.cart = None
    
    def store_activity_to_history(self):
        timestamp = datetime.now()
        temporary_history = user_history(timestamp, self.cart)
        self.history.append(temporary_history)

class event_shopping_cart:
    def __init__(self, quantity, product_id, regular_price, discount_percentage, event_price_with_discount, event_discount_amount):
        self.quantity = quantity
        self.product_id = product_id
        self.regular_price = regular_price
        self.discount_percentage = discount_percentage
        self.event_price_with_discount = event_price_with_discount # amount of the whole event
        self.event_discount_amount = event_discount_amount # amount of the whole event

class user_shopping_cart:
    def __init__(self):
        self.last_event_shopping_cart = None
        self.record = []
        self.list_of_event_product_quantities = []
        self.list_of_event_price_with_discounts = []
        self.list_of_event_discount_amounts = []
        self.total_shopping_cart_products_quantity = None
        self.total_shopping_cart_amount = None
        self.total_shopping_cart_discount_applied_amount = None
    
    def add_last_shopping_cart_event_to_record(self, last_event_shopping_cart):
        self.last_event_shopping_cart = last_event_shopping_cart
        self.list_of_event_product_quantities.append(self.last_event_shopping_cart.quantity)
        self.list_of_event_price_with_discounts.append(self.last_event_shopping_cart.event_price_with_discount)
        self.list_of_event_discount_amounts.append(self.last_event_shopping_cart.event_discount_amount)
        self.total_shopping_cart_products_quantity = sum(self.list_of_event_product_quantities)
        self.total_shopping_cart_amount = sum(self.list_of_event_price_with_discounts)
        self.total_shopping_cart_discount_applied_amount = sum(self.list_of_event_discount_amounts)
        self.record.append(self.last_event_shopping_cart)
    
    def remove_specific_shopping_cart_record_index(self, index):
        index = index - 1 # Python list offset
        del self.list_of_event_product_quantities[index]
        del self.list_of_event_price_with_discounts[index]
        del self.list_of_event_discount_amounts[index]
        del self.record[index]
        self.total_shopping_cart_products_quantity = sum(self.list_of_event_product_quantities)
        self.total_shopping_cart_amount = sum(self.list_of_event_price_with_discounts)
        self.total_shopping_cart_discount_applied_amount = sum(self.list_of_event_discount_amounts)

class user_history:
    def __init__(self, timestamp, full_shopping_cart_sold, total_amount_in_shopping_cart, total_discount_applied_in_shopping_cart):
        self.timestamp = timestamp
        self.full_shopping_cart_sold = full_shopping_cart_sold
        self.total_amount_in_shopping_cart = total_amount_in_shopping_cart
        self.total_discount_applied_in_shopping_cart = total_discount_applied_in_shopping_cart
