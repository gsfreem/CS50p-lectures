def main():
    x, y, z = input('Lets do some basic math: ').split()
    x = float(x)
    z = float(z)

    match y:
        case '*':
            print(round(x * z, 1))
        case '/':
            print(round(x / z, 1))
        case '+':
            print(round(x + z, 1))
        case '-':
            print(round(x - z, 1))

main()