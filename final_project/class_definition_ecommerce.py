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

    def return_to_inventory(self, returned_quantity):
        self.inventory += returned_quantity

class customer:
    def __init__(self, customer_id, entered_name):
        self.customer_id = customer_id
        self.entered_name = entered_name
        self.shopping_cart = None
        self.is_active = False
        self.purchase_history = []

    def shopping_cart_deletion(self):
        self.shopping_cart = None
    
    def store_activity_to_history(self, timestamp, invoice_number):
        self.shopping_cart.timestamp = timestamp
        self.shopping_cart.invoice_number = invoice_number
        self.purchase_history.append(self.shopping_cart)

class shopping_cart:
    def __init__(self):
        self.shopping_cart_events = None
        self.total_shopping_cart_products_quantity = 0
        self.total_shopping_cart_amount = 0
        self.total_shopping_cart_discount_applied_amount = 0
        self.timestamp = None # Only used for confirmed purchase
        self.invoice_number = 0

    def add_articles_to_shopping_cart(self, quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount):
        if (self.shopping_cart_events == None):
            temporal_shopping_cart_event = shopping_cart_event(quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount)
            self.shopping_cart_events = sequential_dict()
            self.shopping_cart_events.add(temporal_shopping_cart_event)
        else:
            if (self.product_id_present(product_id)):
                key = self.get_dict_key_of_product_id(product_id)
                self.shopping_cart_events.dicts[key].quantity = self.shopping_cart_events.dicts[key].quantity + quantity
                self.shopping_cart_events.dicts[key].net_amount = self.shopping_cart_events.dicts[key].net_amount + net_amount
                self.shopping_cart_events.dicts[key].discounted_amount = self.shopping_cart_events.dicts[key].discounted_amount + discounted_amount
            else:
                temporal_shopping_cart_event = shopping_cart_event(quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount)
                self.shopping_cart_events.add(temporal_shopping_cart_event)
        # Totals calculation
        self.total_shopping_cart_products_quantity = sum(instance.quantity for instance in self.shopping_cart_events.dicts.values())
        self.total_shopping_cart_amount = sum(instance.net_amount for instance in self.shopping_cart_events.dicts.values())
        self.total_shopping_cart_discount_applied_amount = sum(instance.discounted_amount for instance in self.shopping_cart_events.dicts.values())

    def product_id_present(self, product_id):
        return_value = False
        for dictionary in self.shopping_cart_events.dicts.values():
            if dictionary.product_id == product_id:
                return_value = True
                break
        return return_value

    def get_dict_key_of_product_id(self, product_id):
        for key, value in self.shopping_cart_events.dicts.items():
            if (value.product_id == product_id):
                dict_key = key
                break
        return key

    def remove_articles_from_shopping_cart(self, key):
        self.shopping_cart_events.remove(key)
        # Totals re-calculation
        self.total_shopping_cart_products_quantity = sum(instance.quantity for instance in self.shopping_cart_events.dicts.values())
        self.total_shopping_cart_amount = sum(instance.net_amount for instance in self.shopping_cart_events.dicts.values())
        self.total_shopping_cart_discount_applied_amount = sum(instance.discounted_amount for instance in self.shopping_cart_events.dicts.values())

class shopping_cart_event:
    def __init__(self, quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount):
        self.quantity = quantity
        self.product_id = product_id
        self.regular_price = regular_price
        self.discount_percentage = discount_percentage
        self.net_amount = net_amount
        self.discounted_amount = discounted_amount


class sequential_dict:
    def __init__(self):
        self.dicts = {}

    def add(self, value):
        key = len(self.dicts) + 1
        self.dicts[key] = value

    def remove(self, key):
        if key in self.dicts:
            del self.dicts[key]

            self.dicts = {index + 1: value[1] for index, value in enumerate(self.dicts.items())}
