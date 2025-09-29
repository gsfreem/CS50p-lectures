def version_1():
    dificulty = input("Please select a dificulty mode -> Easy | Medium | Hard   ")
    
    def dificulty_select(selection):
        match selection:
            case 'Easy' | 'easy':
                youchose("Easy")
            case 'Medium' | 'medium':
                youchose("Medium")
            case 'Hard' | 'hard':
                youchose("Hard")
            case _:
                print('please check you spelling')
    
    def youchose(choice):
        print(f'You have selected -> {choice}')
    
    dificulty_select (dificulty)

def version_2():
    difficulty = input('Please select a difficulty -> Easy | Medium | Hard: ')
    
    def youchose(choice):
        print(f'You chose: {choice}')

    if difficulty == 'Easy' or difficulty == 'easy':
        youchose('Easy')
    elif difficulty == 'Medium' or difficulty == 'medium':
        youchose('Medium')
    elif difficulty == 'Hard' or difficulty == 'hard':
        youchose('Hard')
    else:
        print('Try again')

version_1()