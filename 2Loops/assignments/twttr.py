def main():
    tweet = input('Input: ').strip()
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_tweet = []
    
    for character in tweet:
        if character not in vowels:
            new_tweet.append(character)

    print(f'Output: {''.join(new_tweet)}')

main()