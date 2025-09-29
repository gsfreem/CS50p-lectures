def main():
    old_name = input(': ').strip()
    print(': ', end="")
    snake_caser(old_name)
    
def snake_caser(name):
    
    for character in name:
        if character == character.capitalize():
            print(f'_{character.lower()}', end="")
        else:
            print(character, end="")
             









main()