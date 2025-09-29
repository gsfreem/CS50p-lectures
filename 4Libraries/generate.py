from random import choice as flip
from random import randint as rng
from random import shuffle # shuffles the argument in place
from statistics import mean

def coin_flip():
    coin = ['heads', 'tails']
    print(flip(coin))

def number_generator():
    random_number = rng(1, 10)
    print(random_number)

def shuffler():
    cards = ['jack', 'queen', 'king']
    shuffle(cards)
    for card in cards:
        print(card)

def grad_average():
    grades = [100, 90, 93, 98, 89, 100]
    print(mean(grades))


if __name__ == '__main__':
    ...