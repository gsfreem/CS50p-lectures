import sys

def main():

    name_list = []
    while True:
        try:
            names = input('Name: ').strip().title()
            name_list.append(names)
        except EOFError:
            break

    if len(name_list) < 1:
        sys.exit()
    elif len(name_list) == 1:
        print(f'Adieu, adieu, to {name_list[0]}')
    else:
        for name in name_list:
            if name_list.index(name) == 0:
                print(f'Adieu, adieu, to {name_list[0]}')
            elif name_list.index(name) == 1:
                print(f'Adieu, adieu, to {name_list[0]} and {name_list[1]}')
            else:
                print(f'Adieu, adieu, to {", ".join(name_list[:name_list.index(name)])}, and {name}')
        



if __name__ == '__main__':
    main()