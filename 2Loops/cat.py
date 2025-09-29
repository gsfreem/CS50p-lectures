def main():
    number = get_number()
    meow(number)


def meow(n):
    for _ in range(n): print('meow')


def get_number():
    while True:
        output = int(input('How many cats are in the barn? '))
        if output > 0: break
    return output


main()