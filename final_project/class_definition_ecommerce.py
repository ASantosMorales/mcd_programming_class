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
        self.shopping_cart = None
    
    def store_activity_to_history(self):
        timestamp = datetime.now()
        self.shopping_cart.timestamp = timestamp
        self.history.append(self.shopping_cart)

class shopping_cart:
    def __init__(self):
        self.shopping_cart_events = {}
        self.total_shopping_cart_products_quantity = None
        self.total_shopping_cart_amount = None
        self.total_shopping_cart_discount_applied_amount = None
        self.timestamp = None # Only used for confirmed purchase

    def add_articles_to_shopping_cart(self, quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount):
        if product_id in self.shopping_cart_events:
            temporal_shopping_cart_event = self.shopping_cart_events[product_id]
            temporal_shopping_cart_event.quantity = self.shopping_cart_events[product_id].quantity + quantity
            temporal_shopping_cart_event.net_amount = self.shopping_cart_events[product_id].net_amount + net_amount
            temporal_shopping_cart_event.discounted_amount = self.shopping_cart_events[product_id].discounted_amount + discounted_amount
        else:
            temporal_shopping_cart_event = shopping_cart_event(quantity, regular_price, discount_percentage, net_amount, discounted_amount)
            # Temporal dictionary asignation
            self.shopping_cart_events[product_id] = temporal_shopping_cart_event
        # Totals calculation
        self.total_shopping_cart_products_quantity = sum(instance.quantity for instance in self.shopping_cart_events.values())
        self.total_shopping_cart_amount = sum(instance.net_amount for instance in self.shopping_cart_events.values())
        self.total_shopping_cart_discount_applied_amount = sum(instance.discounted_amount for instance in self.shopping_cart_events.values())

    def remove_articles_from_shopping_cart(self, index):
        index = index - 1 # Python list offset
        # product_id deletion
        del self.shopping_cart_events[index]
        # Totals re-calculation
        self.total_shopping_cart_products_quantity = sum(instance.quantity for instance in self.shopping_cart_events.values())
        self.total_shopping_cart_amount = sum(instance.net_amount for instance in self.shopping_cart_events.values())
        self.total_shopping_cart_discount_applied_amount = sum(instance.discounted_amount for instance in self.shopping_cart_events.values())

class shopping_cart_event:
    def __init__(self, quantity, regular_price, discount_percentage, net_amount, discounted_amount):
        self.quantity = quantity
        self.regular_price = regular_price
        self.discount_percentage = discount_percentage
        self.net_amount = net_amount
        self.discounted_amount = discounted_amount


class sequential_dict:
    def __init__(self):
        self.data = {}

    def add(self, value):
        key = len(self.data) + 1
        self.data[key] = value

    def remove(self, key):
        if key in self.data:
            del self.data[key]

            self.data = {index + 1: value for index, value in enumerate(self.data.items())}

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
