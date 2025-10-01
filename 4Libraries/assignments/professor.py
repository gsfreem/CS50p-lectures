import random

def main():
    selected_level = get_level()
    new_problem_set = generate_integer(selected_level)
    score = 0

    for set in new_problem_set:
        solution = set[0] + set[1]
        lives = 2
        
        while True:
            print(f'{set[0]} + {set[1]} = ', end="")
            try:
                user_answer = int(input("").strip())
                if user_answer != solution: raise ValueError
            except ValueError:
                if lives == 0:
                    print('EEE')
                    print(f'{set[0]} + {set[1]} = {set[0] + set[1]}')
                    break
                else:
                    lives -= 1
                    print('EEE')
                pass
            else:
                score += 1
                break

    print(f'score: {score}')
 

def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input('Level: '))
            if level not in levels: raise ValueError
        except ValueError: pass
        except NameError: pass
        else: return level


def generate_integer(level):
    problem_set = []
    for _ in range(10):
        match level:
            case 1:
                int_1 = random.randint(1, 9)
                int_2 = random.randint(1, 9)
                problem_set.append((int_1, int_2))
            case 2:
                int_1 = random.randint(10, 99)
                int_2 = random.randint(10, 99)
                problem_set.append((int_1, int_2))
            case 3:
                int_1 = random.randint(100, 999)
                int_2 = random.randint(100, 999)
                problem_set.append((int_1, int_2))
    return problem_set
    

if __name__ == "__main__":
    main()