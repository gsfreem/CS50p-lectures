def main():
    fraction = input('Fraction: ')
    conversion = convert(fraction)
    fuel_left = gauge(conversion)
    print(fuel_left)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x.strip())
            y = int(y.strip())
        except NameError:
            pass
        else:
            return (x/y) * 100

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
