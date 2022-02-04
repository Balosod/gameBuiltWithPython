'''
random module form python library
'''
import random
suits = ('Hearts', 'Diamonds', 'Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
        'Seven','Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
        'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
class Card:
    '''
    initializing the  card details using a class
    '''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  
    def __str__(self):
        return self.rank + ' of ' + self.suit
class Deck():
    '''
    creating a deck of all cards
    '''
    def __init__(self):
        self.all_player_decks = []
        for suit in suits:
            for rank in ranks:
                self.all_player_decks.append(Card(suit,rank))
    def shuffle(self):
        '''
        This is a method that shuffled the class deck
        object my importing the random python library
        '''
        random.shuffle(self.all_player_decks)
    def __str__(self):
        for deck in self.all_player_decks:
            return f"{[deck]}"
class Chips:
    '''
    This is a class object that hold the player total bet
    '''
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        '''
        This is a method that was called whenever the
        player won and add the bet value to the
        total value
        '''
        self.total +=self.bet
        print(f'You got additional {self.bet}, your total chips is {self.total}')
    def lose_bet(self):
        '''
        This is a method that was called whenever the
        player lose and subtract the bet value from the
        total value
        '''
        self.total -= self.bet
        print(f'You lose additional {self.bet}, your toal chisps is {self.total}')
class Dealer:
    '''
    This is a class object that hold the Dealer's card
    '''
    def __init__(self):
        self.reserved_card = []
    def add_card (self, card_to_add):
        '''
        This is a method that append a card
        to the dealer's hand
        '''
        self.reserved_card.append(card_to_add)
class Player:
    '''
    This is a class object that hold the Player's card
    '''
    def __init__(self):
        self.reserved_card = []
    def add_card (self, card_to_add):
        '''
        This is a method that append a card
        to the player's hand
        '''
        self.reserved_card.append(card_to_add)
def take_bet(chip):
    '''
    This is a function that take in the chips object an
    argument and prompt the player to take a bet

    '''
    while True:
        try:
            chip.bet = int(input("place your bet: "))
        except:
            print("Enter correct input ")
            continue
        else:
            if  chip.bet > chip.total:
                print("Chip exceeded")
                continue
            break
def hit_or_stand(decs,players,dealers):
    '''
    This is a function that take in three argument which are
    the Deck, Player and Dealer object and promtp the user
    to make a HIT or STAND
    '''
    position = 'wrong'
    while position not in ['HIT', 'STAND']:
        try:
            position = input('Choose to HIT or STAND: ')
        except:
            print('Choose correct syntax')
            continue
        else:
            if position == 'HIT':
                players.add_card(decs.all_player_decks.pop(0))
            if position == 'STAND':
                dealers.add_card(decs.all_player_decks.pop(0))
def show_some(players,dealers):
    '''
    This is a function that shows all the player's hand
    and show only one of the dealer hand
    '''
    for index, tuple in enumerate (players.reserved_card):
        print(f'front view of players card is: {players.reserved_card[index]}')
    for index, tuple in enumerate (dealers.reserved_card):
        print(f'font view of dealers card is: {dealers.reserved_card[-1]}')
        break   
def show_all(players,dealers):
    '''
    This is a function that shows all the player's  and the
    dealer's hand
    '''
    for index, tuple in enumerate (players.reserved_card):
        print(f'front view of players card is: {player.reserved_card[index]}')
    for index, tuple in enumerate (dealers.reserved_card):
        print(f'font view of dealers card is: {dealer.reserved_card[index]}')
def decision():
    '''
    This is a function the promt the player
    if he wishes to continue playing or not
    and return True if YES and return False
    if NO
    '''
    choice = 'wrong'
    while choice not in ['YES','NO']:
        try:
            choice = input('Do you wish to play again, YES or NO: ')

        except:
            print('type correct syntax')
            continue
        else:
            if choice == 'YES':
                return True
            return False
chips  = Chips()
PLAYING = True
GAME = True
while GAME == True:
    dec = Deck()
    i = 0
    print('WELCOME TO BLACKJACK GAME')
    take_bet(chips)
    dec.shuffle()
    player = Player()
    dealer = Dealer()
    for i in range(0,2):
        player.add_card(dec.all_player_decks.pop(0))
        dealer.add_card(dec.all_player_decks.pop(0))
    while PLAYING:
        PLAYER_SUM = 0
        DEALER_SUM = 0
        for index,tuple in enumerate(dealer.reserved_card):
            DEALER_SUM += dealer.reserved_card[index].value
            if DEALER_SUM > 16 and dealer.reserved_card[index].rank == 'Ace':
                DEALER_SUM -= 10
        for index,tuple in enumerate(player.reserved_card):
            PLAYER_SUM += player.reserved_card[index].value
            if PLAYER_SUM > 20 and player.reserved_card[index].rank == 'Ace':
                PLAYER_SUM -= 10
        print(f'dealer sum = {DEALER_SUM}')
        print(f'player sum = {PLAYER_SUM}')
        show_some(player, dealer)
        if PLAYER_SUM > 21:
            print('player busted')
            chips.lose_bet()
            break
        if DEALER_SUM > 21:
            print('dealer busted')
            chips.win_bet()
            break
        if PLAYER_SUM == 21:
            print('player won')
            chips.win_bet()
            break
        if DEALER_SUM == PLAYER_SUM:
            print(f'dealer sum = {DEALER_SUM}')
            print(f'player sum = {PLAYER_SUM}')
            print('You Tied')
            hit_or_stand(dec,player,dealer)
            continue
        if DEALER_SUM < 17:
            hit_or_stand(dec,player,dealer)
        if ((DEALER_SUM >= 17)  and (DEALER_SUM < 22) and (DEALER_SUM > PLAYER_SUM)):
            print('dealer won')
            chips.lose_bet()
            break
        if ((DEALER_SUM >= 17)  and (DEALER_SUM < 22) and (PLAYER_SUM > DEALER_SUM)):
            print('player won')
            chips.win_bet()
            break    
    GAME = False
    show_all(player, dealer)
    GAME = decision() 