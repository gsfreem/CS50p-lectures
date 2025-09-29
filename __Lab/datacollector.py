from tools import typewriter

def main():
    
    typewriter("Hello friend, my name is Scratch." \
    "Since you're new here we need to get you registered." \
    "I'm just going to ask you a few simple questions to get you started.")


    while True:
        new_user = get_info()
        user_name_dict = new_user[0]
        user_name = user_name_dict['name']
        firstname, _ = user_name.split()
        
        if get_verification(new_user) == True:

            typewriter(f"Okay {firstname}, thats all the info I need right now. Thanks for your cooperation. I will see you very soon! :)") 
            break
        
        else:
            typewriter('Looks like we should start over...')
            continue


def get_info():
    user_info = [
    {'name': input('What is your name? ').strip().title()},
    {'age': input('What is your age? ').strip()},
    {'weight': input('What is your weight? ').strip()},
    {'height': input('What is your height? ').strip()},
    {'race': input('What is your race? ').strip()},
    {'address': input('What is your address? ').strip()},
    {'phone #': input('What is your phone number? ').strip()}]
    return user_info
def get_verification(list):
    
    print()
    typewriter("Ok so here is what you gave me...")
    print()

    for item in list:
        for key in item:
            typewriter(f"{key}: {item[key]}")
    
    print()
    
    x = input('Does this information look correct? [yes/no] ').strip().lower()
    match x:
        case 'yes' | 'y':
            return True
        case 'no' | 'n':
            return False
        case _:
            return False
        
    print()


main()