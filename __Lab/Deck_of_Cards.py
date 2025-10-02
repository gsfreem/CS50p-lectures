import random

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f'{self.name} of {self.suit} -> value={self.value}'


def main():
    deck = deck_builder()
    random.shuffle(deck)
    for _ in range(2):
        card = deck.pop(-1)
        print(f'{card.name} of {card.suit}', end=" | ")  
    
    


def deck_builder():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs',]
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
              '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    deck = []

    for suit in suits:
        for value in values:
            card = Card(value, suit, values[value])
            deck.append(card)
    return deck












if __name__ == '__main__':
    main()
