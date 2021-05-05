from collections import Counter
from hand_values import *


# this class define an object to determine the hand value of a list of card
class HandChecker:
    def __init__(self, cards):
        self.cards = cards
        self.values = [h.value for h in cards]
        self.suits = [h.suit for h in cards]

    def check_flush(self):
        if (len(set(self.suits))) == 1:
            return True
        else:
            return False

    def check_straight(self):
        if len(set(self.values)) == 5 and max(self.values) - min(self.values) == 4:
            return True
        else:
            if set(self.values) == set([14, 2, 3, 4, 5]):
                return True
            else:
                return False

    def check_four_of_a_kind(self):
        return sorted(Counter(self.values).values()) == [1, 4]

    def check_full_house(self):
        return sorted(Counter(self.values).values()) == [2, 3]

    def check_three_of_a_kind(self):
        return 3 in Counter(self.values).values()

    def check_two_pairs(self):
        return sorted(Counter(self.values).values()) == [1, 2, 2]

    def check_one_pair(self):
        return 2 in Counter(self.values).values()

    def check_straight_flush(self):
        return self.check_flush() and self.check_straight() and sorted(self.values) != [10, 11, 12, 13, 14]

    def check_royal_flush(self):
        return self.check_flush() and sorted(self.values) == [10, 11, 12, 13, 14]

    # check the value from the highest value to the lowest value
    def check_hand(self):
        if self.check_royal_flush():
            return ROYAL_FLUSH
        if self.check_straight_flush():
            return STRAIGHT_FLUSH
        if self.check_four_of_a_kind():
            return FOUR_OF_A_KIND
        if self.check_full_house():
            return FULL_HOUSE
        if self.check_flush():
            return FLUSH
        if self.check_straight():
            return STRAIGHT
        if self.check_three_of_a_kind():
            return THREE_OF_A_KIND
        if self.check_two_pairs():
            return TWO_PAIRS
        if self.check_one_pair():
            return PAIR
        return HIGH_CARD


if __name__ == '__main__':
    print(sorted(Counter([1, 2, 2, 2, 2]).values()))
    print(3 in Counter([1, 2, 2, 3, 3]).values())
    print(2 in Counter([1, 2, 2, 3, 3]).values())
