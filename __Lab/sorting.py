

user_name = input('Please...what is your first and last name? ').strip().lower()
first_name, last_name = user_name.split(' ')

def main():
    house = sorter(name_converter(first_name, last_name))
    if house == 'N/A':
        print('I...I am so sorry...but you have not been chosen by a Great House. Maybe try a different name?')
    else:
        print(f'You have been chosen by the great house {house}!')
def name_converter(f, l):
    if len(str(f))%2 == 0 and len(str(l))%2 == 0:
        return 1
    elif len(str(f))%2 == 1 and len(str(l))%2 == 1:
        return 2
    elif len(str(f))%2 == 0 and len(str(l))%2 == 1:
        return 3
    elif len(str(f))%2 == 1 and len(str(l))%2 == 0:
        return 4
    else:
        return 3        
def sorter(n): 
    match n:
        case 1:
            return 'Gryffandor'
        case 2:
            return 'Slytherin'
        case 3:
            return 'Ravenclaw'
        case 4:
            return 'Hufflepuff'
        case _:
            return 'N/A'



if __name__ == '__main__':
    main()