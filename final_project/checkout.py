from tools_for_ecommerce import *
from login import active_user
from invoice import invoice_page

def checkout_page():
    while True:
        os.system('clear')
        checkout_cover_page()

        checkout_user_choice = input(identation * ' ' + 'Your choice: ')

        if (validate_checkout_input(checkout_user_choice)):
            if (checkout_user_choice == '2'):
                break
            else:
                invoice_page()
                break
        else:
            invalid_option()

def checkout_cover_page():
    print('\n')
    current_user_id = active_user(users)
    current_user_entered_name = users[current_user_id].entered_name
    print_centered('The tequila is almost yours')
    print_centered('$$$ You are about to checking out $$$')
    print('\n')
    print_centered(f'This is your shopping cart {current_user_entered_name}')
    print('\n')
    print_user_shopping_cart_table_for_checkout(users[current_user_id].shopping_cart)
    print('\n')
    print_centered('Type an option:')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Confirm purchase and get your invoice', 'blue'))
    print(identation * ' ' + '2. ' + colored('Return to your cart', 'red'))
    print('\n')

def print_user_shopping_cart_table_for_checkout(shopping_cart):
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
    print('\n')
    print(18 * ' '+ 'Summary:')
    print(tabulate([[f'Total products:  {shopping_cart.total_shopping_cart_products_quantity}'], \
        [f'Total price (discount applied):  $ {shopping_cart.total_shopping_cart_amount:.2f}'], \
        [f'Total discount applied:  $ {shopping_cart.total_shopping_cart_discount_applied_amount:.2f}']]))

#******************************
#
#          validations
#
#******************************

def validate_checkout_input(input_str):
    pattern = r'^[1-2]$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)