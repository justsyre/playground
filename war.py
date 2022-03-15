'''
Card Class for War
- Suit, Rank, Value
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create card obj
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_card):
        
        if type(new_card) == type([]):
            # List of multiple cards
            self.all_cards.extend(new_card)
        else:
            # For a single card object
            self.all_cards.append(new_card)


    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# GAME LOGIC
## Game Setups
p1 = Player("One")
p2 = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    p1.add_cards(new_deck.deal_one())
    p2.add_cards(new_deck.deal_one())

## Game On
game_on = True
round_cnt = 0

while game_on:
    round_cnt += 1
    print(f"Round {round_cnt}")

    if len(p1.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break

    if len(p2.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break

    #Start a new round
    p1_cards = []
    p1_cards.append(p1.remove_one())

    p2_cards = []
    p2_cards.append(p2.remove_one())

    # War
    at_war = True

    while at_war:
        if p1_cards[-1].value > p2_cards[-1].value:

            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)

            at_war = False
        elif p1_cards[-1].value < p2_cards[-1].value:

            p2.add_cards(p1_cards)
            p2.add_cards(p2_cards)

            at_war = False
        
        else:
            print('WAR!')

            if len(p1.all_cards) < 5:
                print('Player One unable to declare war')
                print('Player Two wins!')
                game_on = False
                break
            elif len(p2.all_cards) < 5:
                print('Player Two unable to declare war')
                print('Player One wins!')
                game_on = False
                break
            else:
                for num in range(5):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())