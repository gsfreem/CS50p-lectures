def main_v1():
    answer = input('What is the answer to the Great Question of Life, the Universe, and Everything? ')
    if answer == '42' or answer == 'Forty-Two' or answer == 'Forty Two' or answer == 'Forty-two' or answer == 'Forty two' or answer == 'forty-two' or answer == 'forty two':
        print('Yes')
    else:
        print('No')

def main_v2():
    answer = input('What is the answer to the Great Question of Life, the Universe, and Everything? ')
    match answer:
        case '42' | 'Forty Two' | 'Forty-Two' | 'Forty two' | 'Forty-two' | 'forty-two' | 'forty two':
            print('Yes')
        case _:
            print('No')


main_v1()
