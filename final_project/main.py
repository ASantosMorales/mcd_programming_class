from functions_for_ecommerce import *

while True:
    os.system('clear')
    user_name_entered = login_page()
    if (validate_user_name(user_name_entered)):
        user_name_id = user_name_format(user_name_entered)
        if not(user_name_already_exists(user_name_id, users)):
            create_user(user_name_id, user_name_entered, users)
        activate_user(user_name_id, users)
        current_user = users[user_name_id]
        home_page()
        deactivate_user(user_name_id, users)
    else:
        bad_user_name()
