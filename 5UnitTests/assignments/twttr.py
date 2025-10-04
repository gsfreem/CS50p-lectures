def main():
    text = input('').strip().split(" ")
    tweet = []
    for word in text:
        tweet.append(shorten(word))
    print(" ".join(tweet))
    


def shorten(word):
    word = word.lower()
    vowels = ['a', 'e', 'u', 'i', 'o',]
    abrev = []
    for letter in word:
        if letter not in vowels:
            abrev.append(letter)
    return ''.join(abrev)

if __name__ == "__main__":
    main()