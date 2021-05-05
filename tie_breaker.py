from hand_values import *
from collections import Counter
from card import Card

# sort the list first, start from the biggest value
def compare_value_list(value1, value2):
    list1 = sorted(list(set(value1)), reverse=True)
    list2 = sorted(list(set(value2)), reverse=True)
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            return True
        elif list1[i] == list2[i]:
            continue
        else:
            return False


# this class create a tie breaker object for two players and provide a list of method for comparing different hand
# values
class TieBreaker:
    def __init__(self, player1, player2):
        self.values1 = [h.value for h in player1.best_hand]
        self.values2 = [h.value for h in player2.best_hand]
        self.value_count1 = Counter(self.values1)
        self.value_count2 = Counter(self.values2)
        self.score1 = player1.score
        self.score2 = player2.score

    # compare two players' best hand value, if tie use the corresponding tie break methods
    # if tie can't be broken return None
    def compare(self):
        if self.score1 is not self.score2:
            if self.score1 > self.score2:
                return True
            elif self.score1 < self.score2:
                return False
        else:
            if self.score1 == HIGH_CARD:
                return self.compare_same_highcard()
            elif self.score1 == PAIR:
                return self.compare_same_pair()
            elif self.score1 == TWO_PAIRS:
                return self.compare_two_pair()
            elif self.score1 == THREE_OF_A_KIND:
                return self.compare_three_of_a_kind()
            elif self.score1 == STRAIGHT:
                return self.compare_straight()
            elif self.score1 == FLUSH:
                return self.compare_flush()
            elif self.score1 == FULL_HOUSE:
                return self.compare_full_house()
            elif self.score1 == FOUR_OF_A_KIND:
                return self.compare_four_of_a_kind()
            elif self.score1 == STRAIGHT_FLUSH:
                return self.compare_straight_flush()
            else:
                return None

    # compare a list of values
    def compare_same_highcard(self):
        return compare_value_list(self.values1, self.values2)

    # compare pair value first, if same compare the kickers
    def compare_same_pair(self):
        for key, value in self.value_count1.items():
            # print(key, value)
            if value == 2:
                pair_value1 = key
        for key, value in self.value_count2.items():
            # print(key, value)
            if value == 2:
                pair_value2 = key

        if pair_value1 > pair_value2:
            return True
        elif pair_value1 < pair_value2:
            return False
        else:
            return compare_value_list(self.values1, self.values2)

    # compare the pair value first, if same compare the kickers
    def compare_two_pair(self):
        pair1 = []
        pair2 = []
        for key, value in self.value_count1.items():
            if value == 2:
                pair1.append(key)
        for key, value in self.value_count2.items():
            if value == 2:
                pair2.append(key)
        if max(pair1) > max(pair2):
            return True
        elif max(pair1) < max(pair2):
            return False
        elif min(pair1) > min(pair2):
            return True
        elif min(pair1) < min(pair2):
            return True
        else:
            return compare_value_list(self.values1, self.values2)

    # compare the triple value first, if same compare the kickers
    def compare_three_of_a_kind(self):
        for key, value in self.value_count1.items():
            if value == 3:
                triple1 = key
        for key, value in self.value_count2.items():
            if value == 3:
                triple2 = key
        if triple1 > triple2:
            return True
        elif triple1 < triple2:
            return False
        else:
            return compare_value_list(self.values1, self.values2)

    # simply compare the biggest value
    def compare_straight(self):
        if max(self.values1) > max(self.values2):
            return True
        elif max(self.values1) < max(self.values2):
            return False

    # the same comparison as high card
    def compare_flush(self):
        return compare_value_list(self.values1, self.values2)

    # compare the threes first then the twos
    def compare_full_house(self):
        for key, value in self.value_count1.items():
            if value == 3:
                triple1 = key
            if value == 2:
                pair1 = key

        for key, value in self.value_count2.items():
            if value == 3:
                triple2 = key
            if value == 2:
                pair2 = key

        if triple1 > triple2:
            return True
        elif triple1 < triple2:
            return False
        elif pair1 > pair2:
            return True
        elif pair1 < pair2:
            return False

    # compare the fours and then the kicker
    def compare_four_of_a_kind(self):
        for key, value in self.value_count1.items():
            if value == 4:
                foursome1 = key
            if value == 1:
                single1 = key

        for key, value in self.value_count2.items():
            if value == 4:
                foursome2 = key
            if value == 1:
                single2 = key

        if foursome1 > foursome2:
            return True
        elif foursome1 < foursome2:
            return False
        elif single1 > single2:
            return True
        elif single1 < single2:
            return False

    # same as straight
    def compare_straight_flush(self):
        return self.compare_straight()


# a test main function
if __name__ == '__main__':
    card1 = [Card("6", "D"), Card("5", "D"), Card("4", "S"), Card("3", "S"), Card("2", "C")]
    card2 = [Card("6", "D"), Card("5", "D"), Card("4", "S"), Card("3", "S"), Card("2", "C")]
    card3 = [Card("6", "D"), Card("6", "D"), Card("6", "S"), Card("6", "S"), Card("2", "C")]
    card4 = [Card("4", "D"), Card("4", "D"), Card("4", "S"), Card("4", "S"), Card("2", "C")]

    print(TieBreaker(card3, card4).compare_four_of_a_kind())
