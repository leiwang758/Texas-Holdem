from itertools import combinations
from card import Card


# this class define a community object, including community cards and it's all possible 3-card combos
class CommunityCard:
    def __init__(self, cards):
        self.cards = self.create_cards(cards)
        self.combos = list(combinations(self.cards, 3))

    def get_handvalue(self, hand):
        return list(combinations(self.cards, 3)) + hand

    def create_cards(self, cards):
        return list(Card(card[0], card[1]) for card in cards)
