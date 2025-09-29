def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    hash = '#'
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print(hash * i, hash * i, sep="")
        
if __name__ == '__main__':
    main()