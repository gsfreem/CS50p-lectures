import random


def main():
    selected_level = get_level() # prompts the user to select a level
    score = 0                                               
    
    for _ in range(10):
        x = generate_integer(selected_level)
        y = generate_integer(selected_level)
        
        solution = x + y
        lives = 3
        
        while True:
            try:
                if lives == 0: raise SyntaxError
                user_answer = int(input(f'{x} + {y} = ').strip())
                if user_answer != solution: raise ValueError
                else: score += 1
            except ValueError:
                print('EEE')
                lives -= 1
            except SyntaxError:
                print(f'{x} + {y} = {solution}')
                break 
            else:
                break

    print(f'Score: {score}')


def get_level():
    levels = [1, 2, 3]

    while True:
        try:
            level = int(input('Level: ').strip())
            if level not in levels: raise ValueError
        except ValueError:
            pass
        else:
            return level
def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
if __name__ == "__main__":
    main()