from check_hands import HandChecker
from card import Card


# this class define a player object, including name, hands, possible combos from community, best hand, best score,
# print kicker flag and rank
def create_cards(cards):
    return list(Card(card[0], card[1]) for card in cards)


class Player:
    def __init__(self, name, cards, combos):
        self.name = name
        self.cards = create_cards(cards)
        self.combos = combos
        self.rank = 0
        self.best_hand, self.score = self.get_highest_hand()
        self.print_kickers = False

    # get current best hand based on hand cards and community cards
    def get_highest_hand(self):
        max_hand = []
        max_value = -1
        for c in self.combos:
            hand = list(c) + self.cards
            value = HandChecker(hand).check_hand()
            if value > max_value:
                max_value = value
                max_hand = hand
        return max_hand, max_value

    def set_rank(self, rank):
        self.rank = rank

    # set the print kicker flag, which means if it's necessary to print out the kicker info
    def set_print_kickers(self, print_kicker):
        self.print_kickers = print_kicker
