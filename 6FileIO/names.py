def write_to_text_file():
    while True:
        try:
            name = input('What is your name? ').lower().strip()
            if name == 'none':
                raise EOFError
        except EOFError:
            name = None
            break
        else:
            with open('names.txt', 'a') as file:
                file.write(f'{name}\n')
def read_text_file():
    names = []
    with open('names.txt', 'r') as file:
        for line in file:
            names.append(line.capitalize().rstrip())
    for name in sorted(names):
        print(f'Hello, {name}')


if __name__ == '__main__':
    write_to_text_file()
    read_text_file()