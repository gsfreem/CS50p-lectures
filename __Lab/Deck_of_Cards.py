import random

names = {'Joker':0, 'One':1, 'Two':2, 'Three':3, 'Four':4, 
         'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 
         'Jack':10, 'Queen':10, 'King':10, 'Ace':10}

suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

class Card:
    def __innit__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value