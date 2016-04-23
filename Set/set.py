from setFunctions import *
from datetime import datetime

class Set:
    def __init__(self):
        deck,board,graveyard = init() #Initialise variables
        end_game = False
        message = ''
        start_time = datetime.now()
        while not end_game:
            end_game, quit_game, message = self.game_loop(deck, board, graveyard, end_game, message)
        self.end(start_time, deck, board, graveyard, quit_game)

    def game_loop(self, deck, board, graveyard, end_game, message):
        display_board(board)
        quit_game = False
        print('Deck:', len(deck), 'cards')
        print('Board:', len(board), 'cards')
        print('Graveyard:', len(graveyard), 'cards','\n')
        print(message,'\n')
        print('1: Pick a Set | 2: Declare Set absence | 3: Quit game')
        menu = input()
        print('')

        if menu == '3':
            end_game = True
            quit_game = True
        elif menu == '2':
            if not exists_set(board):
                board,deck,end_game = case_I(board,deck)
                if not end_game:
                    message = 'Added 3 cards from deck to board'
            else:
                deck,graveyard = case_II(deck,graveyard)
                message = 'Set present! 3 card penalty'
        elif menu == '1':
            selected_cards = select_set(board)
            if selected_cards != None:
                if is_set(selected_cards):
                    board,deck,graveyard = case_III(board,deck,graveyard,selected_cards)
                    message = 'Set found!'
                else:
                    message = 'Not a Set...'
            else:
                message = 'Player cancelled pick or entered invalid values'
        else:
            message = 'Invalid value'

        return end_game, quit_game, message

    def end(self, start_time, deck, board, graveyard, quit_game):    
        end_time = datetime.now()
        delta = float((end_time-start_time).total_seconds())
        delta = round(delta,1)

        if quit_game:
            print('Player ended game','\n')
        elif len(graveyard) == 81:
            print('Player won! All cards in graveyard','\n')
        else:
            print('Player won! No Sets in play','\n')
    
        print('Deck:',len(deck),'cards')
        print('Board:',len(board),'cards')
        print('Graveyard:',len(graveyard),'cards')
        print('Game time:',delta,'seconds')