numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    plate = input('Plate: ' )
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(plate):
    
    indexes = range(len(plate))
    if len(plate) < 2 or len(plate) > 6: 
        return False
    if plate[0] in numbers or plate[1] in numbers: 
        return False 
    for index in indexes:
        if plate[index] == '0' and plate[index - 1] in letters: 
            return False
    for index in indexes: 
        if plate[index] in numbers and plate[index+1:index + 2] in letters:
            return False
    for character in plate: 
        if character not in numbers and character not in letters: 
            return False
    return True

if __name__ == "__main__":
    main()