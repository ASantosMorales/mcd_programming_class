from tools_for_ecommerce import *

def login_page():
    print_banner()
    print('\n')
    print_centered('Welcome!!!')
    print('\n')
    print_centered('To enter, type your first name and your family name')
    print_centered('separated by a space.')
    print('\n')
    return (input(identation * ' ' + 'Your name: '))

def print_banner():
    print("  ___        ___ ___  _ __ ___  _ __ ___   ___ _ __ ___ ___")
    print(" / _ \\_____ / __/ _ \\| '_ ` _ \\| '_ ` _ \\ / _ \\ '__/ __/ _ \\")
    print("|  __/_____| (_| (_) | | | | | | | | | | |  __/ | | (_|  __/")
    print(" \\___|      \\___\\___/|_| |_| |_|_| |_| |_|\\___|_|  \\___\\___|")

def exit_message():
    os.system('clear')
    print('\n')
    print('\n')
    print('\n')
    print_centered('Thank you, see you next time!')
    print('\n')
    print('\n')
    print('\n')
    time.sleep(2)

#******************************
#
#          validations
#
#******************************

def validate_user_name(input_str):
    pattern = r'^[a-zA-Z\s]+$'
    if re.match(pattern, input_str):
        validation = True
    else:
        validation = False
    return (validation)

def user_name_format(user_name):
    user_name = user_name.replace(' ', '_').lower()
    return (user_name)

def user_name_already_exists(user_name, users_dictionary):
    already_exists = False
    if user_name in users_dictionary:
        already_exists = True
    return(already_exists)

def create_user(user_name_formated, user_name_entered, users_dictionary):
    users_dictionary[user_name_formated] = customer(user_name_formated, user_name_entered, specific_user_shopping_cart)

def activate_user(user_name, users_dictionary):
    users_dictionary[user_name].is_active = True

def deactivate_user(user_name, users_dictionary):
    users_dictionary[user_name].is_active = False

def active_user(users_dictionary):
    _active_user = None
    for user in users_dictionary.values():
        if user.is_active == True:
            _active_user = user.customer_id
            break
    return (_active_user)

def bad_user_name():
    print('\n')
    print_centered('Name is invalid.')
    print('\n')
    print_centered('Only letters and spaces are allowed here.')
    time.sleep(2)