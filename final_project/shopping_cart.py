def adding_to_cart(user_choice):
    print('\n')
    print_centered('How many bottles do you want to add to your car?')
    product_id_user_choice = int(user_choice)
    inventory = products[product_id_user_choice].inventory
    print_centered(f'Maximum of Tequila {product_id_user_choice} bottles is {inventory}')
    while True:
        print('\n')
        quantity_to_cart = input(identation * ' ' + 'Type the number of bottles: ')
        if (validate_products_quantity(quantity_to_cart)):
            quantity_to_cart = int(quantity_to_cart)
            if (validate_inventory(quantity_to_cart, inventory)):
                """
                total_price_with_discount = round(quantity_to_cart * products[item_user_choice].price_with_discount, 2)
                total_discount_amount = round(quantity_to_cart * products[item_user_choice].discount_amount, 2)
                adding_to_cart_transaction(quantity_to_cart, item_user_choice, products[item_user_choice].price, products[item_user_choice].discount, total_price_with_discount, total_discount_amount)
                """
                adding_to_cart_transaction(quantity_to_cart, product_id_user_choice)
                print('\n')
                print_centered(f'You added {quantity_to_cart} bottles of Tequila {product_id_user_choice} to your cart.')
                print('\n')
                print_centered("Let's continue shopping!!!")
                time.sleep(2)
                break
            else:
                print('\n')
                print_centered('You exceded the stock, try again!')
        else:
            invalid_option()

"""
def adding_to_cart_transaction(quantity, product_id, regular_price, discount_percentage, total_price_with_discount, total_discount_amount):
    current_user_id = active_user(users)
    current_user = users[current_user_id].adding_to_cart(quantity, product_id, regular_price, discount_percentage, total_price_with_discount, total_discount_amount)
"""
def adding_to_cart_transaction(quantity, product_id):
    regular_price = products[product_id].regular_price
    discount_percentage = products[product_id].discount_percentage
    event_price_with_discount = quantity * products[product_id].price_with_discount
    event_discount_amount = quantity * products[product_id].discount_amount
    temporal_event_shopping_cart = event_shopping_cart(quantity, product_id, regular_price, discount_percentage, event_price_with_discount, event_discount_amount)
    specific_user_shopping_cart.add_last_shopping_cart_event_to_record(temporal_event_shopping_cart)

def cart_page():
    while True:
        os.system('clear')
        cart_cover_page()

        cart_user_choice = input(identation * ' ' + 'Your choice: ')
        
        if (validate_cart_input(cart_user_choice)):
            if (cart_user_choice == '1'):
                checkout_page()
                break
            if (cart_user_choice == '2'):
                edit_cart_section()
            else:
                break
        else:
            invalid_option()

def cart_cover_page():
    print('\n')
    current_user_id = active_user(users)
    current_user_entered_name = users[current_user_id].entered_name
    print_centered(f'This is your shopping cart {current_user_entered_name}')
    print('\n')
    print_user_cart_table(users[current_user_id])
    print('\n')
    print_centered('Type an option:')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Go to checkout', 'blue'))
    print(identation * ' ' + '2. ' + colored('Remove items', 'blue'))
    print(identation * ' ' + '3. ' + colored('Go to home', 'red'))
    print('\n')

def print_user_cart_table(current_user):
    headers = ['Ref', 'Quantity', 'Product', 'Unit price', '% Discount', 'Final price']
    table = []
    index = 1
    for shopping_cart in current_user.cart.record:
        table.append([f'{index}', \
                    f'{shopping_cart.quantity}', \
                    f'Tequila_{shopping_cart.product_id}', \
                    f'$ {(products[shopping_cart.product_id].price):.2f}', \
                    f'{shopping_cart.discount_percentage} %', \
                    f'$ {shopping_cart.event_price_with_discount:.2f}'])
        index += 1
    print(tabulate(table, headers, tablefmt = 'simple', stralign = 'center', numalign = 'center'))
    print('\n')
    print(18 * ' '+ 'Summary:')
    print(tabulate([[f'Total products:  {current_user.total_products_in_shopping_cart}'], [f'Total price (discount applied):  $ {current_user.total_amount_in_shopping_cart:.2f}'], [f'Total discount applied:  $ {current_user.total_discount_applied_in_shopping_cart:.2f}']]))

def edit_cart_section():
    print('\n')
    print_centered('Type the row number you want to remove... ')
    print('\n')
    while True:
        edit_cart_user_choice = input(identation * ' ' + 'Your selection: ')
        if (validate_edit_cart_input(edit_cart_user_choice)):
            edit_cart_user_choice = int(edit_cart_user_choice)
            current_user_id = active_user(users)
            rows_in_user_cart = get_rows_number_in_cart(current_user_id)
            if (edit_cart_user_choice <= rows_in_user_cart):
                user_cart_row_deletion(current_user_id, edit_cart_user_choice)
                break
            else:
                invalid_option()
        else:
            invalid_option()

def user_cart_row_deletion(current_user_id, edit_cart_user_choice):
    print('\n')
    print_centered(f'You are about to delete row {edit_cart_user_choice},')
    print_centered('are you sure?')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Yes', 'blue'))
    print(identation * ' ' + '2. ' + colored('No, I want to keep the products', 'red'))
    print('\n')
    user_confirm_deletion_choice = input(identation * ' ' + 'Your selection: ')
    if (validate_confirm_deletion(user_confirm_deletion_choice)):
        if (user_confirm_deletion_choice == '1'):
            quantity = users[current_user_id].cart[edit_cart_user_choice - 1].quantity
            total_price_with_discount = users[current_user_id].cart[edit_cart_user_choice - 1].total_price_with_discount
            total_discount_amount = users[current_user_id].cart[edit_cart_user_choice - 1].total_discount_amount
            users[current_user_id].remove_from_cart(quantity, price_with_discount, discount_amount)
            del users[current_user_id].cart[edit_cart_user_choice - 1]
    else:
        invalid_option()

def get_rows_number_in_cart(current_user_id):
    return (len(users[current_user_id].cart))

#******************************
#
#          validations
#
#******************************

def validate_cart_input(input_str):
    pattern = r'^[1-3]$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)

def validate_edit_cart_input(input_str):
    pattern = r'^\d+$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)

def validate_confirm_deletion(input_str):
    pattern = r'^[1-2]$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)