# asks the user to define two variables and defines the user input as an 
# integer data type
# then adds those two values together
a = int(input("What's a? "))
b = int(input("What's b? "))
print(a + b)


# does the same thing as above but the data type is now floating point
c = float(input("""Now lets try something more complicated. 
Give me some decimals. What's c? """))
d = float(input("What's d? "))

# rounds the decimal to the nearest 2 digits
answer = round(c + d, 2)

# prints the answer in a formated string
print(f"{answer:,}")

