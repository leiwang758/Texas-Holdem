from hand_values import *
from collections import Counter


def get_value_name(v):
    if v == 14:
        return "Ace"
    elif v == 13:
        return "King"
    elif v == 12:
        return "Queen"
    elif v == 11:
        return "Jack"
    elif v == 10:
        return "T"
    else:
        return str(v)


# this class define a printer object for a given player
class DescriptionPrinter:
    def __init__(self, player):
        self.name = player.name
        self.cards, self.score = player.get_highest_hand()
        self.rank = player.rank
        self.values = sorted([c.value for c in self.cards], reverse=True)
        self.value_names = [get_value_name(v) for v in self.values]
        self.suits = [c.suit for c in self.cards]
        self.value_count = Counter(self.value_names)
        self.suit_count = Counter(self.suits)
        self.description = ""
        self.kickers = ""
        self.print_kicker = player.print_kickers

    # print out all description and kickers if necessary
    def print_description(self):
        self.set_description()
        print("{rank} {name} {description}".format(rank=self.rank, name=self.name, description=self.description),
              end='')
        if self.print_kicker and self.kickers is not None:
            self.print_kickers()
        else:
            print('')

    # set current player's description and kickers info based on their hand value
    def set_description(self):
        if self.score == HIGH_CARD:
            self.description = "high card"
            self.kickers = self.value_names
        elif self.score == PAIR:
            kickers = []
            for key, value in self.value_count.items():
                if value == 2:
                    pair_name = key
                else:
                    kickers.append(key)
            self.description = "Pair {name}".format(name=pair_name)
            self.kickers = kickers
        elif self.score == TWO_PAIRS:
            pairs = []
            for key, value in self.value_count.items():
                if value == 2:
                    pairs.append(key)
                else:
                    self.kickers = [key]
            self.description = "Two Pair " + ' '.join(pairs)
        elif self.score == THREE_OF_A_KIND:
            kickers = []
            for key, value in self.value_count.items():
                if value == 3:
                    triple_name = key
                else:
                    kickers.append(key)
            self.description = "Three {name}s".format(name=triple_name)
            self.kickers = kickers
        elif self.score == STRAIGHT:
            self.description = "Straight {name}".format(name=self.value_names[0])
            self.kickers = None
        elif self.score == FLUSH:
            self.description = "{name}-high Flush".format(name=self.value_names[0])
            self.kickers = self.value_names
        elif self.score == FULL_HOUSE:
            for key, value in self.value_count.items():
                if value == 3:
                    triple_name = key
                elif value == 2:
                    pair_name = key
            self.description = "Full house, {tname} full of {pname}".format(tname=triple_name, pname=pair_name)
            self.kickers = None
        elif self.sore == FOUR_OF_A_KIND:
            for key, value in self.value_count.items():
                if value == 4:
                    foursome_name = key
                else:
                    kicker = key
            self.description = "Four {name}s with a {kicker}".format(name=foursome_name, kicker=kicker)
            self.kickers = [kicker]
        elif self.score == STRAIGHT_FLUSH:
            self.description = "{name}-high Straight Flush".format(name=self.value_names[0])
            self.kickers = None
        elif self.score == ROYAL_FLUSH:
            self.description = "ROYAL FLUSH"

    # print out a formatted kicker info
    def print_kickers(self):
        print(", with {kickers} as kicker(s)".format(kickers=', '.join(self.kickers)))
