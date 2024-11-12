def products_page():
    while True:
        os.system('clear')
        products_cover_page()

        product_user_choice = input(identation * ' ' + 'Your choice: ')
        
        if (validate_products_input(product_user_choice)):
            if (product_user_choice == '9'):
                break
            else:
                adding_to_cart(product_user_choice)
        else:
            invalid_option()

def products_cover_page():
    print('\n')
    print_centered('Here you can see our products.')
    print_centered('Type the number ID you want to select')
    print_centered('Enjoy!')
    print('\n')
    print_products_table()
    print('\n')
    print(identation * ' ' + '9. ' + colored('Go home page', 'red'))
    print('\n')

def print_products_table():
    headers = ['ID', 'Product', 'Regular price', 'Discount', 'Final price', 'Stock']
    table = []
    for key, item in products.items():
        table.append([f'{key}', f'Tequila_{key}', f'$ {item.regular_price:.2f}', f'{item.discount_percentage} %', f'$ {item.price_with_discount:.2f}', f'{item.inventory} bottles'])
    print(tabulate(table, headers, tablefmt = 'simple', stralign = 'center', numalign = 'center'))

#******************************
#
#          validations
#
#******************************

def validate_products_input(input_str):
    pattern = r'^[1-9]$'
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


#******************************
#
#      products creation
#
#******************************

random.seed(1)
products = {}
for index in range(1, 9):
    products[index] = product(round(random.uniform(300, 2500), 2), random.randint(5, 50), random.choice([0, 10, 15, 25, 30, 50]))