# Tic-Tac-Toe

import random

def drawBoard (board) :
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print (board[7] + '|' + board[8] + '|' + board[9])
    print ('-+-+-')
    print (board[4] + '|' + board[5] + '|' + board[6])
    print ('-+-+-')
    print (board[1] + '|' + board [2] + '|' + board[3])

def inputPlayerLetter () :
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == '0') :
        print ('Do you want to be X or 0?')
        letter = input().upper()

    # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X' :
        return ['X','O']
    else :
        return ['O', 'X']

def whoGoesFirst () :
    # Randomly choose the player who goes first.
    if random.randint(0,1) == 0 :
        return 'computer'
    else :
        return 'player'
    
def makeMove (board, letter, move) :
    board[move] = letter

def isWinner (bo, le) :
    # Given a board and a player's letter, this function returns True if that player has won.
    # I used bo and le instead of board and letter so I don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
