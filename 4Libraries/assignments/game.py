import random

def main():
    while True:
        try:
            dificulty = int(input('Level: ').strip())
            if dificulty < 0:
                raise ValueError
        except ValueError:
            pass
        except NameError:
            pass
        else:
            break

    secret_number = random.randint(1, dificulty)
    
    while True:
        try:
            user_guess = int(input('Guess: '))
            if user_guess == secret_number:
                return print('Just right!')
            if user_guess < 1:
                raise ValueError
        except ValueError:
            pass
        except NameError:
            pass
        else:
            if user_guess < secret_number:
                print('Too small!')
            elif user_guess > secret_number:
                print('Too large!')


if __name__ == '__main__':
    main()