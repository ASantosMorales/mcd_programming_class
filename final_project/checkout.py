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
    print_user_cart_table(users[current_user_id])
    print('\n')
    print_centered('Type an option:')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Generate PayPal link', 'blue'))
    print(identation * ' ' + '2. ' + colored('Generate MercadoPago link', 'blue'))
    print(identation * ' ' + '3. ' + colored('Return to your cart', 'red'))
    print('\n')

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