def main():
    dollars = dollars_to_float(input("How much was your meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f} as a tip!")
def dollars_to_float(meal_price):
    return float(meal_price.strip("$"))
def percent_to_float(des_tip):
    des_tip = float(des_tip.strip("%"))
    return float(des_tip/100)
main()