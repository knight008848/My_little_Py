#!/usr/bin/env python

'''
Class sample 2
'''

import random

# define globals for cards
RANKS= ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS= ["Clubs", "Diamonds", "Hearts", "Spades"]

def quick_sort(L):
    if len(L) <= 1:
        return L
    else:
        pivot = L[0]
        left, right = [], []
        for x in L[1:]:
            if x < pivot:
                left.append(x)
            elif x >= pivot:
                right.append(x)

        return quick_sort(left) + [pivot] + quick_sort(right)

class Card(object):
    """docstring for Card"""
    def __init__(self, suit, rank):
        super(Card, self).__init__()
        self.rank = rank - 1
        self.suit = suit - 1

    def __str__(self):
        return '%s of %s' % (RANKS[self.rank], SUITS[self.suit])

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

class Deck(object):
    """docstring for Deck"""
    def __init__(self):
        self.cards = [Card(s, r) for r in range(1,14)for s in range(1,5)]
        # for suit in range(1,5):
        #     for rank in range(1,14):
        #         card = Card(suit, rank)
        #         self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __len__(self):
        return len(self.cards)

class Hand(Deck):
    """docstring for Hand"""


if __name__ == "__main__":
    card1 = Card(1,12)
    card2 = Card(1,10)
    card3 = Card(3,10)

    deck = Deck()
    deck.shuffle()
    print deck
    deck.sort()
    print deck