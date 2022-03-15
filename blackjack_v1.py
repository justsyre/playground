'''
Black Jack

Objective : Get a closer value to a value of 21 than the dealer
Computer Dealer vs Player

Actions :   • Hit - recieve another card from the DECK
            • Stay - stop recieving cards
'''
import random
from string import capwords

# GLOBAL VARIBLES
## Variable that will be used to create a deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create a card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop() # Returns a single card

class Hand():

    def __init__(self):
        self.cards = [] # Starts as an empty list
        self.value = 0 # Starts as 0
        self.aces = 0 # Add an attribute to keep track of aces

    def add_card(self, card):

        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

## Test
# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# test_player.value


class Chips:
    
    def __init__(self):
        self.total = 100 # Default value or can be also supplied by the user
        self.bet = 0

    def win_bet(self):

        self.total = self.total + (self.bet*2) # If the user win the bet is doubled and added to the total
    
    def lose_bet(self):

        self.total = self.total - self.bet # If player loses he only lose the number of bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Please enter a bet: '))
        except ValueError:
            print('Sorry a bet must be a number or integer')
        else:
            if chips.bet > chips.total:
                print(f'Sorry your bet cannot exceeds {chips.total}')
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing # control the while loop, by default playing is True
    
    while True:

        player_input = input("Would you like to Hit or Stand? 'h' or 's': ")

        if player_input.lower() == 'h':
            hit(deck, hand)
        elif player_input.lower() == 's':
            print('Player Stand! Dealers turn')
            playing = False
        else:
            print('Please try again!')
            continue
        break
    
    # while playing:
    #     try:
    #         player_input = str(input('Hit or Stand? (h or s)').lower)
    #         if player_input == 'h' or player_input == 'hit':
    #             hit(deck, hand)
    #             print('Player Hit')
    #         elif player_input == 's' or player_input == 'stand':
    #             print('Player Stand')
    #             playing = False
    #     except:
    #         print('General Error Occured!, Check your input.')

def show_some(player, dealer):

    print('\nDealers Hand: ')
    print('<hidden card>')
    print('',dealer.cards[1])
    print('\nPlayers Hand: ', *player.cards, sep = '\n')

def show_all(player, dealer):

    print('\nDealers Hand:', *dealer.cards, sep = '\n')
    print('Dealers Value = ',dealer.value)
    print('\nPlayer Hand:', *player.cards, sep = '\n')
    print('Player Value =  ',player.value)

def player_busts(player, dealer, chips):
    print('Player Bust')
    chips.lose_bet()

def player_win(player, dealer, chips):
    print('Player Win')
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print('Dealer Bust')
    chips.lose_bet()

def dealer_win(player, dealer, chips):
    print('Dealer Win')
    chips.win_bet()

def push(player, dealer):
    print('Dealer and Player is tie! PUSH')




### GAME LOGIC ###
while True:
    print('\n')
    print('••• Simplified Black Jack •••')
    print('\nGet as close as possible to 21 as you can without Dealer hits until reaches 17.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Setup Player Chips
    player_chips = Chips() # by default player has 100 Chips
    
    # Prompt player for their Bet
    take_bet(player_chips)

    # Show cards (note one of Dealer cards is hidden)
    show_some(player_hand, dealer_hand)

    while playing: # this is True recall the variable from hit_or_stand()
        
        # Prompt player if hit or stand
        hit_or_stand(deck, player_hand)

        # Show cards (note one of Dealer cards is hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        # Show all players hand
        show_all(player_hand, dealer_hand)

        # Winning Scenario
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            player_win(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value <= 21:
            player_win(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value <= 21:
            dealer_win(player_hand, dealer_hand)

        else:
            push(player_hand, dealer_hand)
        
        # Inform player of the total Chips
        print(f'Player has a total of {player_chips.total}')

        # Ask to play again

        new_game = input('Play Again? (y or n): ')

        if  new_game.lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing")
            break