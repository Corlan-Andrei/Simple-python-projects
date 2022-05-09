import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has:" +deck_comp

    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        return self.deck.pop()

# test_deck = Deck()
# print(test_deck)
# so far so good, the deck works.

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips shall you bet?:"))
        except:
            print("Try again, with numbers this time.")
        else:
            if chips.bet > chips.total:
                print("You cannot bet more than your allowance. Try again.")
            else:
                break


def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand?: ').lower()
        if x[0] == "h":
            hit(deck,hand)

        elif x[0] == "s":
            print("The player stands! It's the dealer's turn.")
            playing = False

        else:
            print("Please try again.")
            continue
        break

# man I'm glad I don't play poker or whatever, these rules and actions are weird

def show_some(player,dealer):
    print(f"Dealer's Hand: -hidden card-, {dealer.cards[1]}")


def show_all(player,dealer):
    print("Dealer's hand:", *dealer.cards )
    print(f"Value of Dealer's cards is {dealer.value}")
    print("\n Player's hand:", *player.cards)
    print(f"Value of Player's hand is {player.value} ")


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts! The player wins!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push():
    print("Dealer and Player have tied! PUSH!")


# OK, functions are all done, time for the logic of the rest of the app.

while True:
    # Welcome statement:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player:
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips:
    player_chips = Chips()  # remember the default value is 100

    # Prompt the Player for their bet:
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden):
    show_some(player_hand,dealer_hand)

    while playing:  # recall this variable from the hit_or_stand function

        # Prompt for Player to Hit or Stand:
        hit_or_stand(deck,player_hand)

        # Show cards (but keep one dealer card hidden):
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop:
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17:
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Show all cards:
        show_all(player_hand,dealer_hand)

        # Check different winning scenarios:
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their total chips:
    print("\nPlayer's winnings stand at",player_chips.total)

    # Ask to play again:
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


   # init_player_val = values[player_hand[0]] + values[player_hand[1]]
   # init_dealer_val = values[dealer_hand[0]] + values[dealer_hand[1]]

   # if init_player_val > 21:
   #     print('The player was given two cards with a total sum over 21. The player loses.')
   #     break
   # elif init_dealer_val

   # The above commented section was if an initial card combination could be over 21. It is no longer useful.
