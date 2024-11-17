from tools_for_ecommerce import *
from login import active_user

def store_history_in_log_file(invoice_number, date, time, entered_name, shopping_cart):
	current_user_id = active_user(users)
	log_file_name = f'{current_user_id}_log_file.txt'
	new_event_to_log = build_full_event(invoice_number, date, time, entered_name, shopping_cart)
	if (log_file_exists(log_file_name)):
		append_new_event_to_log_file(log_file_name, new_event_to_log)
	else:
		create_log_file_and_add_new_event(log_file_name, new_event_to_log)


def build_full_event(invoice_number, date, time, entered_name, shopping_cart):
	full_event = get_invoice_purchase_data_table(invoice_number, date, time, entered_name)
	full_event = full_event + '\n' + get_invoice_products_table(shopping_cart)
	full_event = full_event + '\n' + get_invoice_total_table(shopping_cart) + '\n'
	return (full_event)

def log_file_exists(file_name):
	return_data = False
	if os.path.exists(file_name):
		return_data = True
	return (return_data)

def append_new_event_to_log_file(file_name, new_event):
	with open(file_name, 'a') as file:
		file.write(new_event)

def create_log_file_and_add_new_event(file_name, new_event):
	with open(file_name, 'w') as file:
		file.write(new_event)

def get_invoice_purchase_data_table(invoice_number, date, time, entered_name):
	table = [[f'Invoice No. {invoice_number}'], [f'Date: {date} {time}'], [f'Customer Name: {entered_name}']]
	table_to_print = tabulate(table, tablefmt = 'rst', stralign = 'left')
	return (table_to_print)

def get_invoice_products_table(shopping_cart):
	headers = ['Ref', 'Quantity', 'Product', 'Unit price', '% Discount', 'Final price']
	table = []
	for key, shopping_cart_event in shopping_cart.shopping_cart_events.dicts.items():
		table.append([f'{key}', \
					f'{shopping_cart_event.quantity}', \
					f'Tequila_{shopping_cart_event.product_id}', \
					f'$ {(shopping_cart_event.regular_price):.2f}', \
					f'{shopping_cart_event.discount_percentage} %', \
					f'$ {shopping_cart_event.net_amount:.2f}'])
	table_to_print = tabulate(table, headers, tablefmt = 'simple', stralign = 'center', numalign = 'center')
	return (table_to_print)

def get_invoice_total_table(shopping_cart):
	table = [[f'Subtotal (discount applied) = $ {shopping_cart.total_shopping_cart_amount:.02f}'], 
			[f'Total discounted amount = $ {shopping_cart.total_shopping_cart_discount_applied_amount:.02f}'], 
			['Taxes = $ 0.00'], 
			[f'Total = $ {shopping_cart.total_shopping_cart_amount:.02f}']]
	table_to_print = tabulate(table, tablefmt = 'rst', stralign = 'left')
	return (table_to_print)