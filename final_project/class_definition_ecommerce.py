from datetime import datetime

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
    def __init__(self, customer_id, entered_name):
        self.customer_id = customer_id
        self.entered_name = entered_name
        self.shopping_cart = None
        self.is_active = False
        self.purchase_history = []

    def shopping_cart_deletion(self):
        self.shopping_cart = []
    
    def store_activity_to_history(self):
        timestamp = datetime.now()
        self.timestamp = timestamp
        self.history.append(shopping_cart)

class shopping_cart:
    def __init__(self):
        self.quantity = []
        self.product_id = []
        self.regular_price = []
        self.discount_percentage = []
        self.net_amount = []
        self.discounted_amount = []
        self.total_shopping_cart_products_quantity = None
        self.total_shopping_cart_amount = None
        self.total_shopping_cart_discount_applied_amount = None
        self.timestamp = None # Only used for confirmed purchase

    def add_articles_to_shopping_cart(self, quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount):
        self.quantity.append(quantity)
        self.product_id.append(product_id)
        self.regular_price.append(regular_price)
        self.discount_percentage.append(discount_percentage)
        self.net_amount.append(net_amount)
        self.discounted_amount.append(discounted_amount)
        self.total_shopping_cart_products_quantity = sum(self.quantity)
        self.total_shopping_cart_amount = sum(self.net_amount)
        self.total_shopping_cart_discount_applied_amount = sum(self.discounted_amount)

    def remove_articles_from_shopping_cart(self, index):
        index = index - 1 # Python list offset
        del self.quantity[index]
        del self.product_id[index]
        del self.regular_price[index]
        del self.discount_percentage[index]
        del self.net_amount[index]
        del self.discounted_amount[index]
        self.total_shopping_cart_products_quantity = sum(self.quantity)
        self.total_shopping_cart_amount = sum(self.net_amount)
        self.total_shopping_cart_discount_applied_amount = sum(self.discounted_amount)

"""
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
    def __init__(self, timestamp, full_shopping_cart_sold):
        self.timestamp = timestamp
        self.full_shopping_cart_sold = full_shopping_cart_sold
"""
