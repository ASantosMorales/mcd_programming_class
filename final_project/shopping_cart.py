from tools_for_ecommerce import *
from products import *
from login import active_user
from checkout import checkout_page

def adding_to_cart(user_choice):
    print('\n')
    print_centered('How many bottles do you want to add to your car?')
    product_id_user_choice = int(user_choice)
    inventory = products_dict[product_id_user_choice].inventory
    print_centered(f'Maximum of Tequila {product_id_user_choice} bottles is {inventory}')
    while True:
        print('\n')
        quantity_to_cart = input(identation * ' ' + 'Type the number of bottles: ')
        if (validate_products_quantity(quantity_to_cart)):
            quantity_to_cart = int(quantity_to_cart)
            if (validate_inventory(quantity_to_cart, inventory)):
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

def adding_to_cart_transaction(quantity, product_id):
    current_user_id = active_user(users)
    regular_price = products_dict[product_id].regular_price
    discount_percentage = products_dict[product_id].discount_percentage
    net_amount = quantity * products_dict[product_id].price_with_discount
    discounted_amount = quantity * products_dict[product_id].discount_amount
    if (users[current_user_id].shopping_cart == None):
        users[current_user_id].shopping_cart = shopping_cart()
    users[current_user_id].shopping_cart.add_articles_to_shopping_cart(quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount)

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
    print_user_shopping_cart_table(users[current_user_id])
    print('\n')
    print_centered('Type an option:')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Go to checkout', 'blue'))
    print(identation * ' ' + '2. ' + colored('Remove items', 'blue'))
    print(identation * ' ' + '3. ' + colored('Go to home', 'red'))
    print('\n')

def print_user_shopping_cart_table(current_user):
    headers = ['Ref', 'Quantity', 'Product', 'Unit price', '% Discount', 'Final price']
    table = []
    index = 1
    for shopping_cart_index in range(get_rows_number_in_shopping_cart(users[current_user])):
        table.append([f'{index}', \
                    f'{users[current_user].shopping_cart.quantity[shopping_cart_index]}', \
                    f'Tequila_{users[current_user].shopping_cart.product_id[shopping_cart_index]}', \
                    f'$ {users[current_user].shopping_cart.regular_price[shopping_cart_index]:.2f}', \
                    f'{users[current_user].shopping_cart.discount_percentage[shopping_cart_index]} %', \
                    f'$ {users[current_user].shopping_cart.net_amount[shopping_cart_index]:.2f}'])
        index += 1
    print(tabulate(table, headers, tablefmt = 'simple', stralign = 'center', numalign = 'center'))
    print('\n')
    print(18 * ' '+ 'Summary:')
    print(tabulate([[f'Total products:  {users[current_user].shopping_cart.total_shopping_cart_products_quantity}'], \
        [f'Total price (discount applied):  $ {users[current_user].shopping_cart.total_shopping_cart_amount:.2f}'], \
        [f'Total discount applied:  $ {users[current_user].shopping_cart.total_shopping_cart_discount_applied_amount:.2f}']]))

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
            removing_event_from_cart_transaction(current_user_id, edit_cart_user_choice)
    else:
        invalid_option()

def removing_event_from_cart_transaction(current_user_id, edit_cart_user_choice):
    users[current_user_id].cart.remove_specific_shopping_cart_record_index(edit_cart_user_choice)

def get_rows_number_in_shopping_cart(current_user):
    return (len(current_user.shopping_cart.quantity))

def retreive_shopping_cart_data_by_index(shopping_cart_row, index):
    if (shopping_cart_row.quantity == []):
        quantity = 0
        product_id = 0
        regular_price = 0
        discount_percentage = 0
        net_amount = 0
        discounted_amount = 0
    else:
        quantity = shopping_cart_row.quantity[index]
        product_id = shopping_cart_row.product_id[index]
        regular_price = shopping_cart_row.regular_price[index]
        discount_percentage = shopping_cart_row.discount_percentage[index]
        net_amount = shopping_cart_row.net_amount[index]
        discounted_amount = shopping_cart_row.discounted_amount[index]
    return (quantity, product_id, regular_price, discount_percentage, net_amount, discounted_amount)

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

def validate_products_quantity(input_quantity):
    pattern = r'^\d+$'
    if re.match(pattern, input_quantity):
        validation = True
    else:
        validation = False
    return (validation)

def validate_inventory(input_quantity, inventory_quantity):
    inventory_ok = False
    if input_quantity <= inventory_quantity:
        inventory_ok = True
    return (inventory_ok)