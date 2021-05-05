import functools
from community_cards import CommunityCard
from player import Player
from tie_breaker import TieBreaker
from description_printer import DescriptionPrinter


# validate the input card
def validate_input_card(input_card):
    if len(input_card) != 2:
        return False
    if input_card[0] not in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
        return False
    if input_card[1] not in ["H", "S", "D", "C"]:
        return False
    else:
        return True


# get user input and validate it
def get_user_input():
    print("\n\n=====================================================")
    print("================== Texas Hold'em ====================")
    print("=====================================================\n\n")
    while True:
        community_cards = list(map(str, input("Please enter the community card (separated by space):\n").split()))
        if len(community_cards) != 5 or not all(validate_input_card(c) for c in community_cards):
            print("Invalid input!, please try again")
            continue
        else:
            while True:
                num_player = input("How many players will be playing ?\n")
                if not num_player.isnumeric() or int(num_player) < 2 or int(num_player) > 10:
                    print("Invalid input!, please try again")
                    continue
                else:
                    break

            i = 0
            player_list = []
            while i < int(num_player):
                player = list(map(str, input("Add a player and their hole cards:\n").split()))
                if len(player) != 3 or not all(validate_input_card(card) for card in player[1:]):
                    print("Invalid input!, please try again")
                    continue
                player_list.append(player)
                i += 1

            print("Input complete!\n\n")
            return community_cards, player_list


# rank players based on the compare function defined below
def rank_players(players):
    players.sort(key=functools.cmp_to_key(compare), reverse=True)
    players[0].set_rank(1)
    for i in range(len(players) - 1):
        if TieBreaker(players[i + 1], players[i]).compare() is not None:
            players[i + 1].set_rank(i + 2)
        else:
            players[i + 1].set_rank(players[i].rank)


# compare function used to rank players' score, if tie then set print_kicker flag to true
def compare(player1, player2):
    if player1.score == player2.score:
        player1.set_print_kickers(True)
        player2.set_print_kickers(True)
    if TieBreaker(player1, player2).compare() is True:
        return 1
    elif TieBreaker(player1, player2).compare() is False:
        return -1
    elif TieBreaker(player1, player2).compare() is None:
        return 0


if __name__ == '__main__':
    ## uncomment this and comment get_user_input() to use the sample input
    # print("\n\n=====================================================")
    # print("================== Texas Hold'em ====================")
    # print("=====================================================\n\n")
    # c, p_list = ['KS', 'AD', '3H', '7C', 'TD'], [['John', '9H', '7S'], ['Sam', 'AC', 'KH'], ['Becky', 'JD', 'QC'],
    #                                              ['Lei', 'AD', 'QC'], ['Leii', 'KS', '3H']]


    ## get user input for community card and players' hand
    c, p_list = get_user_input()
    community_card = CommunityCard(c)

    # create a list of player object
    player_list = list(Player(p[0], p[1:], community_card.combos) for p in p_list)

    # rank players based on their best hand
    rank_players(player_list)

    # print out the ranking info, including kickers if necessary
    print("======================= Rank ========================")
    for p in player_list:
        DescriptionPrinter(p).print_description()
    print("=====================================================")
