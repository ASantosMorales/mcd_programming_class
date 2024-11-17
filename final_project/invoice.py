from tools_for_ecommerce import *
from login import active_user

def invoice_page():
    os.system('clear')
    timestamp = datetime.now()
    date = f'{timestamp.day:02}/{timestamp.month:02}/{timestamp.year}'
    time = f'{timestamp.hour:02}:{timestamp.minute:02}:{timestamp.second:02}'
    current_user_id = active_user(users)
    print_invoice_header(80)
    print_invoice_purchase_data(date, time, users[current_user_id].entered_name)
    print_invoice_table(users[current_user_id].shopping_cart)
    print_invoice_total(users[current_user_id].shopping_cart)
    inventory_update(users[current_user_id].shopping_cart)
    user_shopping_cart_update(users[current_user_id])
    print('\n')
    print_centered('Thanks for shopping with us!')
    print('\n')
    input('Press Enter to continue... ')

def print_invoice_header(length_table):
	print(length_table * '=')
	invoice_text = 'Invoice'
	print((int(length_table/2) - len(invoice_text))* ' ' + invoice_text)
	print(length_table * '=')

def print_invoice_purchase_data(date, time, entered_name):
	table = [[f'Invoice No. {random.randint(1, 1000)}'], [f'Date: {date} {time}'], [f'Customer Name: {entered_name}']]
	print(tabulate(table, tablefmt = 'rst', stralign = 'left'))

def print_invoice_table(shopping_cart):
	headers = ['Ref', 'Quantity', 'Product', 'Unit price', '% Discount', 'Final price']
	table = []
	for key, shopping_cart_event in shopping_cart.shopping_cart_events.dicts.items():
		table.append([f'{key}', \
					f'{shopping_cart_event.quantity}', \
					f'Tequila_{shopping_cart_event.product_id}', \
					f'$ {(shopping_cart_event.regular_price):.2f}', \
					f'{shopping_cart_event.discount_percentage} %', \
					f'$ {shopping_cart_event.net_amount:.2f}'])
	print(tabulate(table, headers, tablefmt = 'simple', stralign = 'center', numalign = 'center'))

def print_invoice_total(shopping_cart):
	table = [[f'Subtotal (discount applied) = $ {shopping_cart.total_shopping_cart_amount:.02f}'], ['Taxes = $ 0.00'], [f'Total = $ {shopping_cart.total_shopping_cart_amount:.02f}']]
	print(tabulate(table, tablefmt = 'rst', stralign = 'left'))

def inventory_update(shopping_cart):
    for shopping_cart_event in shopping_cart.shopping_cart_events.dicts.values():
        temporal_product_id = shopping_cart_event.product_id
        temporal_product_quantity = shopping_cart_event.quantity
        products_dict[temporal_product_id].purchasing(temporal_product_quantity)
    
def user_shopping_cart_update(user_context):
    user_context.store_activity_to_history()
    user_context.shopping_cart_deletion()