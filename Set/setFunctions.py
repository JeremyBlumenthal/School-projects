from os import system, name
from random import shuffle
from time import sleep

BOARD_COLUMNS = 3
BOARD_ROWS = 4
CSI = '\x1B['

#Card parameters
elements = {
    0: 1,
    1: 2,
    2: 3
    }
symbols = {
    0 : chr(9762),
    1 : chr(9822),
    2 : chr(9806)
    }
fillings = {
    0: 'F',
    1: 'S',
    2: 'E'
    } #Full, stippled, empty
    
if name == 'posix':
    colors = {0:31, 1:32, 2:34} #Red, blue, green
elif name == 'nt':
    colors = {0:'R', 1:'B', 2:'G'} #Windows alternative

def init():
    '''
    Initialises deck, board and graveyard
    '''
    deck = [[i,j,k,l] for i in range(3) for j in range(3) for k in range(3) for l in range(3)]
    shuffle(deck)
    board = []
    graveyard = []
    
    for i in range(BOARD_ROWS*BOARD_COLUMNS):
        board.append(deck[i])
        del(deck[i])
        
    return deck,board,graveyard

def display_board(board):
    '''
    Display board with BOARD_COLUMNS cards per line
    '''
    if name == 'nt':
        system('cls')
    elif name == 'posix':
        system('clear')
    
    print('Board:')
    new_board = board[:]
    if len(new_board) < (BOARD_COLUMNS*BOARD_ROWS):
        new_board.extend(((BOARD_COLUMNS*BOARD_ROWS)-len(new_board))*chr(10060))
        
    i = 0
    for card in new_board:
        if i % BOARD_COLUMNS == 0:
            print('')
        print(print_card(card),end = '\t')
        i += 1
    print('\n')

def select_set(board):
    '''
    Player picks a Set, verifies choice encoding, converts choices to board indexes and Player confirms choice
    '''
    choice = input('Pick 3 cards (grid format e.g.: 11 12 13):')
    print('')
    cards = []
    pick = []
    length = len(board)
    rows = BOARD_ROWS
    while length > BOARD_ROWS * BOARD_COLUMNS: #Adds a row if board is extended
        rows += 1
        length -= BOARD_COLUMNS
    
    #Choice encoding verification
    if len(choice) == 8:
        if choice[2] == ' ' and choice[5] == ' ':
            choice = choice[:2] + choice[3:5] + choice[6:]
            if choice.isdigit():
                if choice[0:2] != choice[2:4] and choice[2:4] != choice[4:6] and choice[0:2] != choice[4:6]:
                    for i in range(0,len(choice),2):
                        if (int(choice[i]) >= 1 and int(choice[i]) <= rows) and (int(choice[i+1]) >= 1 and int(choice[i+1]) <= BOARD_COLUMNS):
                            pick.append([int(choice[i]),int(choice[i+1])])
                            
    #Conversion to board indexes
    if len(pick) == 3:
        for card in pick:
            index = ((card[0] - 1) * BOARD_COLUMNS) + (card[1] - 1)
            cards.append(board[index])
            print(print_card(board[index]), end=' ')
        confirmation = input(': Type c to confirm, anything else to cancel: ')
        print('')
        if confirmation != 'c':
            cards = None
            
    else:
        cards = None
        
    return cards

def is_set(cards):
    '''
    Checks if cards form a Set
    '''
    Set = False
    if (attributes(cards[0],cards[1],cards[2],0) and attributes(cards[0],cards[1],cards[2],1) 
       and attributes(cards[0],cards[1],cards[2],2) and attributes(cards[0],cards[1],cards[2],3)):
        Set = True
    return Set

def attributes(card0,card1,card2,attribute):
    '''
    Checks if cards have all the same or all different attributes
    '''
    return (card0[attribute]+card1[attribute]+card2[attribute])%3 == 0

def print_card(card):
    '''
    Formats card into a string representing the card's attributes
    '''
    color = colors[card[3]]
    filling = fillings[card[2]]
    element = elements[card[0]]
    symbol = symbols[card[1]]
    new_card = filling + (element * symbol)
    
    if name == 'posix':
        new_card = CSI + str(color) + "m" + new_card + CSI + "0m"
    elif name == 'nt': #Windows alternative
        new_card = color + new_card

    return new_card

def exists_set(card_list):
    '''
    Checks Set possibility on board
    '''
    Set = False
    for i in card_list:
        if not Set:
            for j in card_list:
                if i != j and not Set:
                    for k in card_list:
                        if k != j and k != i and not Set:
                            if is_set([i,j,k]):
                                Set = True
    return Set

def case_I(board,deck):
    '''
    Adds 3 cards from deck to board, ends game if deck is empty
    '''
    if deck == []:
        end_game = True
    else:
        board.extend(deck[:3])
        del deck[:3]
        end_game = False
    return board,deck,end_game

def case_II(deck,graveyard):
    '''
    Adds 3 random cards from graveyard to deck (if graveyard isn't empty)
    '''
    if graveyard != []:
        shuffle(graveyard)
        deck.extend(graveyard[:3])
        del graveyard[:3]
    return deck,graveyard

def case_III(board,deck,graveyard,selected_cards):
    '''
    Selected cards removed from board and added to graveyard, 3 cards added to board from deck (non empty)
    '''
    graveyard.extend(selected_cards)
    for card in selected_cards:
        board.remove(card)
    if deck != []:
        board.extend(deck[:3])
        del deck[:3]
    return board,deck,graveyard
