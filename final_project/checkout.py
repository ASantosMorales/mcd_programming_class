from tools_for_ecommerce import *
from login import active_user
from payment import payment_confirmation_page

def checkout_page():
    while True:
        os.system('clear')
        checkout_cover_page()

        checkout_user_choice = input(identation * ' ' + 'Your choice: ')

        if (validate_checkout_input(checkout_user_choice)):
            if (checkout_user_choice == '3'):
                break
            else:
                payment_confirmation_page(checkout_user_choice)
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
    print_centered(f'This is your cart {current_user_entered_name}')
    print('\n')
    print_user_shopping_cart_table_for_checkout(users[current_user_id])
    print('\n')
    print_centered('Type an option:')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Generate PayPal link', 'blue'))
    print(identation * ' ' + '2. ' + colored('Generate MercadoPago link', 'blue'))
    print(identation * ' ' + '3. ' + colored('Return to your cart', 'red'))
    print('\n')

def print_user_shopping_cart_table_for_checkout(current_user):
    headers = ['Ref', 'Quantity', 'Product', 'Unit price', '% Discount', 'Final price']
    table = []
    index = 1
    for shopping_cart in current_user.cart.record:
        table.append([f'{index}', \
                    f'{shopping_cart.quantity}', \
                    f'Tequila_{shopping_cart.product_id}', \
                    f'$ {(products_dict[shopping_cart.product_id].regular_price):.2f}', \
                    f'{shopping_cart.discount_percentage} %', \
                    f'$ {shopping_cart.event_price_with_discount:.2f}'])
        index += 1
    print(tabulate(table, headers, tablefmt = 'simple', stralign = 'center', numalign = 'center'))
    print('\n')
    print(18 * ' '+ 'Summary:')
    print(tabulate([[f'Total products:  {current_user.cart.total_shopping_cart_products_quantity}'], [f'Total price (discount applied):  $ {current_user.cart.total_shopping_cart_amount:.2f}'], [f'Total discount applied:  $ {current_user.cart.total_shopping_cart_discount_applied_amount:.2f}']]))

#******************************
#
#          validations
#
#******************************

def validate_checkout_input(input_str):
    pattern = r'^[1-3]$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)