def main():
    x = get_integer()
    print(f'x is {x}')


def get_integer():

    # A way to continualy ask for input until a proper input is given from the user
    while True:
        try:
            x = int(input('What is x: '))
        except ValueError:
            print('x is not an integer!')
        else: # note return also acts as the keyword break
            return x





if __name__ == '__main__':
    main()
