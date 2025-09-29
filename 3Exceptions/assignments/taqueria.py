def main():

    total = 0
    menue = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # prompt user for item, adds price of item to toal, prints total
    while True:
        try:
            item = input('Item: ').strip().title()

            if item not in menue:
                raise SyntaxError
            
            price = menue.get(item)
            total = total + price
            print(f'Total: ${total:.2f}')
        except SyntaxError:
            pass
        except EOFError:
            break

main()