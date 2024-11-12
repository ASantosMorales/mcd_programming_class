def home_page():
    while True:
        os.system('clear')
        current_user_id = active_user(users)
        home_cover_page(current_user_id)

        home_user_choice = input(identation * ' ' + 'Your choice: ')

        if validate_home_input(home_user_choice):
            if (home_user_choice == '1'):
                products_page()
            elif(home_user_choice == '2'):
                cart_page()
            elif(home_user_choice == '3'):
                history_page()
            else:
                break
        else:
            invalid_option()
    exit_message()

def home_cover_page(current_user_id):
    current_user_entered_name = users[current_user_id].entered_name
    print_banner()
    print('\n')
    print_centered(f'Welcome {current_user_entered_name}!')
    print('\n')
    print_centered('Please, type an option:')
    print('\n')
    print(identation * ' ' + '1. ' + colored('Go to our products', 'blue'))
    print(identation * ' ' + '2. ' + colored('See your cart', 'blue'))
    print(identation * ' ' + '3. ' + colored('Your history', 'blue'))
    print(identation * ' ' + '4. ' + colored('Exit', 'red'))
    print('\n')

#******************************
#
#          validations
#
#******************************

def validate_home_input(input_str):
    pattern = r'^[1-4]$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)