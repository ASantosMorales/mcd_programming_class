from tools_for_ecommerce import *
from login import active_user

def payment_confirmation_page(payment_method):
    inventory_update()
    user_cart_update()
    os.system('clear')
    print('\n')
    print_centered('Please, go to the next link to complete your payment:')
    print('\n')
    print_centered(random_payment_link_generator(payment_method))
    print('\n')
    print('\n')
    print_centered('Once the payment is processed you will receive')
    print_centered('a confirmation for the shipment.')
    print('\n')
    print_centered('Thanks for shopping with us!')
    print('\n')
    input('Press Enter to continue... ')

def random_payment_link_generator(payment_method):
    random_string_lenght = 15
    chars = string.ascii_letters + string.digits
    random_char = ''
    for index in range(random_string_lenght):
        random_char = random_char + random.choice(chars)

    if (payment_method == 1):
        payment_link = f'www.paypal.com/payment/{random_char}'
    else:
        payment_link = f'www.mercadopago.com/payment/{random_char}'
    return (payment_link)

def inventory_update():
    current_user_id = active_user(users)
    for shopping_cart in users[current_user_id].cart.record:
        products_dict[shopping_cart.product_id].purchasing(shopping_cart.quantity)

def user_cart_update():
    current_user_id = active_user(users)
    users[current_user_id].store_activity_to_history()
    users[current_user_id].cart_deletion()