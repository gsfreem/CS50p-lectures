def coke_machine():
    amount_paid = 0
    amount_due = 50
    
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        payment = int(input(f'Insert Coin: '))
        match int(payment):
            case 25 | 10 | 5:
                amount_paid += payment
                amount_due -= payment
            case _:
                pass

    if amount_due <= 0:
        change = amount_paid - 50
        print(f'Change Owed: {change}')


    
























if __name__ == '__main__':
    coke_machine()