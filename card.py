def get_value(v):
    if v == "T":
        return 10
    elif v == "J":
        return 11
    elif v == "Q":
        return 12
    elif v == "K":
        return 13
    elif v == "A":
        return 14
    else:
        return int(v)


# this class define a card object, specifically it replaces the card value with real comparable numbers
class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = self.get_value(value)
