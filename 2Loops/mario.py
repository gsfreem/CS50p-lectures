def main():
    print_square(20)

def printcolumn(height):
    print('#\n' * height, end='')
def printrow(width):
    print('?' * width)
def print_square(size):
    for i in range(size):
        print('#  ' * size)


        








if __name__ == '__main__':
    main()