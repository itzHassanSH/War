# Card class
# Deck class
# Player class

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
from random import shuffle
from colorama import Fore

# Each player has a deck of cards --> 26 each - in total 52 cards
# A card has suit (heart, diamond, spade, clove), rank (2, 3, 4 ,5 -- King) and value (corresponding integer value)
# A deck has 52 unique card classes --> initialise a list of cards, each having its unique instance

class Card:
    global values
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        print(Fore.GREEN + f"{len(self.cards)} Cards:" + Fore.RESET)
        for _ in range(len(self.cards)):
            print(self.cards[_])
        return ""

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_card(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return Fore.CYAN + f"Player {self.name} has {len(self.cards)} cards" + Fore.RESET


def main():
    card_deck = Deck()
    card_deck.shuffle()

    player_one = Player(input("Enter Player 1's name: "))
    player_two = Player(input("Enter Player 2's name: "))

    for x in range(26):
        player_one.add_cards(card_deck.deal())
        player_two.add_cards(card_deck.deal())

    game_on = True
    round_num = 0
    while game_on:
        round_num += 1
        print(f"Currently on round {round_num}")

        if len(player_one.cards) == 0:
            print(f"{player_two.name} wins!")
            break
        elif len(player_two.cards) == 0:
            print(f"{player_one.name} wins!")
            break

        # START NEW ROUND
        p1_draw = [player_one.remove_card()]
        p2_draw = [player_two.remove_card()]

        # WHILE AT WAR (we assume there's war, and break out if no war)
        at_war = True
        while at_war:
            if p1_draw[-1].value > p2_draw[-1].value:
                player_one.add_cards(p1_draw)
                player_one.add_cards(p2_draw)
                at_war = False
            elif p1_draw[-1].value < p2_draw[-1].value:
                player_two.add_cards(p1_draw)
                player_two.add_cards(p2_draw)
                at_war = False
            else:
                # WAR STARTS HERE
                print("War!")
                if len(player_one.cards) < 5 or len(player_two.cards) < 5:
                    if len(player_one.cards) > len(player_two.cards):
                        player_one.add_cards(p2_draw + p1_draw)
                        print("Player 2 unable to play on")
                    else:
                        player_two.add_cards(p1_draw + p2_draw)
                        print("Player 1 unable to play on")
                    game_on = False
                    break
                else:
                    for i in range(min(5, len(player_one.cards), len(player_two.cards))):
                        p1_draw.append(player_one.remove_card())
                        p2_draw.append(player_two.remove_card())


if __name__ == "__main__":
    main()