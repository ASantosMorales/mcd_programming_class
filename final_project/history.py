from tools_for_ecommerce import *
from login import active_user
from invoice import print_invoice_purchase_data, print_invoice_table, print_invoice_total

def history_page():
    os.system('clear')
    current_user_id = active_user(users)
    current_user_entered_name = users[current_user_id].entered_name
    print('\n')
    print_centered(f'This is your history in our store {current_user_entered_name}')
    print('\n')
    print_history_table(users[current_user_id].purchase_history, current_user_entered_name)
    print('\n')
    input('Press Enter to go to home... ')

def timestamp_to_str(timestamp):
    string_value = f'{timestamp.year}/{timestamp.month:02}/{timestamp.day:02}\n{timestamp.hour:02}:{timestamp.minute:02}:{timestamp.second:02}'
    return (string_value)

def rebuild_products_in_history(quantity, price_with_discount):
    return (f'{quantity} bottles, Tequila_X $ {price_with_discount:.2f}')

def print_history_table(purchase_history, entered_name):
    for purchase_event in purchase_history:
        timestamp = purchase_event.timestamp
        date = f'{timestamp.day:02}/{timestamp.month:02}/{timestamp.year}'
        time = f'{timestamp.hour:02}:{timestamp.minute:02}:{timestamp.second:02}'
        print_invoice_purchase_data(purchase_event.invoice_number, date, time, entered_name)
        print_invoice_table(purchase_event)
        print_invoice_total(purchase_event)
        print('\n')