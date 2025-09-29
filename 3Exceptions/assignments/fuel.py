def main():
    
    while True:
        try:
            x, y = input('Fraction: ').split("/")
            x = x.strip(" ")
            y = y.strip(" ")
            fuel_left = round((int(x)/int(y)) * 100)
            if fuel_left > 100:
                raise SyntaxError
            if fuel_left < 0:
                raise SyntaxError
            break

        except ValueError:
            print('ValueError! Please try again.')
        except SyntaxError:
            print('FuelOverflowError! Please get a mop!')
        except ZeroDivisionError:
            print('ZeroDivisionError! Please try again.')
    
    if fuel_left >= 99:
        print('F')
    elif fuel_left <= 1:
        print('E')
    else:
        print(f'{fuel_left}%')    

main()