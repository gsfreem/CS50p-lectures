import emoji
def main():
    
    word = input('Emoji: ')
    print(f'Output: {emoji.emojize(word, language='alias')}')

if __name__ == '__main__':
    main()