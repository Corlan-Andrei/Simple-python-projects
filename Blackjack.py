import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):

        random.shuffle(self.deck)


    def deal_card(self):

        return self.deck.pop()


class Player:
    # ability to gain and lose chips(money)
    # player can hit, stand, pick betting amount. Make sure bet does not exceed available chips.
    # if player hasn't Bust yet after Hitting, ask if they want to Hit again
    def __init__(self,chips=100):
        self.deck = []
        self.chips = chips

    def add_card(self,new_cards):
        self.deck.append(new_cards)

    def remove_card(self):
        return self.deck.pop()

    def add_chips(self,amount):
        self.chips = self.chips + amount
        return self.chips

    def remove_chips(self,amount):
        self.chips = self.chips - amount
        return self.chips


class Dealer:
    # create automated dealer; give ability to show a single card to player from a 'hand' of two
    # if player Stands, play dealer hand. Dealer will always Hit until Dealer hand value meets or exceeds 17.
    def __init__(self):
        self.deck = []

    def add_card(self,new_cards):
         self.deck.append(new_cards)

    def remove_card(self):
        return self.deck.pop()


player = Player()
dealer = Dealer()

new_deck = Deck()
new_deck.shuffle()

for x in range(2):
    player.add_card(new_deck.deal_card())
    dealer.add_card(new_deck.deal_card())

round_count = 0
game_on = True

player_hand = []
dealer_hand = []
player_bet = 0

for x in range(2):
    dealer_hand.append(dealer.remove_card())
    player_hand.append(player.remove_card())


# I really need to decide on whether I want to use f-string literals or formatting

while game_on:

    round_count += 1

    if player.chips == 0:
        print('Player has no more chips, thus they have lost!')
        break

    while player_bet == 0:

        player_bet = int(input("Bet an amount!"))

        if player_bet > player.chips():

            print("You cannot bet more than your current balance.")
            player_bet = int(input("Bet an amount!"))

    hit_stand = str(input(f"{player_bet} chip bet accepted. Now, do you want to Hit or Stand? ").lower())

    while hit_stand not in ["hit",'stand']:

        hit_stand = input("Choose between Hit and Stand: ")

    result_player = 0
    result_dealer = 0

    while "hit" in hit_stand:
        print(f'Your current bet is of {player_bet} chips.')
        print(f"The Dealer has a {dealer_hand[0]}")
        print(f"You have in your hand a {player_hand[0]} and {player_hand[1]}")

        for card in player_hand:
            result_player = result_player + values[card]

        print(f"The current sum of your card values is {result_player}"

        if result_player > 21:
            hit_stand = "bust"
            if "bust" in hit_stand:
                print("You have busted with a value of {}! You lose this round.".format(result_player))
                player.remove_chips(player_bet)

        player_hand.append(new_deck.deal_card())
        continue_playing = input("Do you wish to continue playing?(Y/N)" ).upper
                if continue_playing in ["Y","N"]:
                    if continue_playing == "Y":
                        continue
                    else:
                        game_on = False
        hit_stand = input("Do you still want to Hit or do you want to Stand? ")


    while "stand" in hit_stand:

        for card in dealer_hand:
            result_dealer = result_dealer + values[card]

            if result_dealer > result_player < 21:
                print("The dealer has a sum of {}, while the player has {}. The dealer wins this round!".format(result_dealer,result_player))
                player.remove_chips(player_bet)
                break
            else:
                hit_stand = "bust"
                if "bust" in hit_stand:
                    print("The dealer busted with a value of {}! The dealer loses the round.".format(result_dealer))
                    player.add_chips(player_bet)
        dealer_hand.append(new_deck.deal_card())
