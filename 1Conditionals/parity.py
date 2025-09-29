def main():
    x  = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0: # can also be written as-> return True if n % 2 == 0 else False or return n % 2 == 0
        return True
    else:
        return False
main()