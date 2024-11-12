def history_page():
    os.system('clear')
    current_user_id = active_user(users)
    current_user_entered_name = users[current_user_id].entered_name
    print('\n')
    print_centered(f'This is your history in our store {current_user_entered_name}')
    print('\n')
    print_history_table(users[current_user_id].history)
    print('\n')
    input('Press Enter to go to home... ')

def timestamp_to_str(timestamp):
    string_value = f'{timestamp.year}/{timestamp.month:02}/{timestamp.day:02}\n{timestamp.hour:02}:{timestamp.minute:02}:{timestamp.second:02}'
    return (string_value)

def rebuild_products_in_history(quantity, product_id, price_with_discount):
    return (f'{quantity} bottles, Tequila_{product_id} $ {price_with_discount:.2f}')

def print_history_table(current_user_history):
    headers = ['Timestamp', 'Total products sold', 'Total payment', 'Total discount']
    table = []
    details = []
    for event in current_user_history:
        text_total_products = ''
        for detail in event.shopping_cart_sold:
            text_total_products = text_total_products + rebuild_products_in_history(detail.quantity, detail.product_id, detail.quantity * detail.price_with_discount) + '\n'
        table.append([timestamp_to_str(event.timestamp), text_total_products, f'$ {event.total_amount_in_shopping_cart:.2f}', f'$ {event.total_discount_applied_in_shopping_cart:.2f}'])
    print(tabulate(table, headers, tablefmt = 'grid', stralign = 'center', numalign = 'center'))