def square(n):
    return n * n


def main():
    x = int(input("Give me a number to square "))
    print (f"{x} squared is ", square(x), sep="")


main()