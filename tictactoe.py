#### Tic Tac Toe - First Milestone Project ####

# test_board = ['#','X','O','X','O','O','O','X','O','X']

## 1 Function to Print Board
def display_board(board):

    print(board[7]+' | '+board[8]+' | '+board[9])
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(board[1]+' | '+board[2]+' | '+board[3])

    print('\n'*2)
# display_board(test_board)



## 2 Function to take Input
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# player_input()


## 3 Function to place input on the board
def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)

## 4 Function to check if the game is won, lost or ongoing
def win_check(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or 
    (board[1] == board[4] == board[7] == mark) or 
    (board[2] == board[5] == board[8] == mark) or 
    (board[3] == board[6] == board[9] == mark) or 
    (board[1] == board[5] == board[9] == mark) or 
    (board[3] == board[5] == board[7] == mark))

# display_board(test_board)
# win_check(test_board,'X')

## 5 Repeat 3 and 4 until game is won or tied

## Choose who is the player going first
import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

## Check free space on the board
def space_check(board, position):

    return board[position] == ' ' or board[position] == ''


## Check the board if it is full
def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False

    return True

## Ask for player next postion and use space_check to see if postion is free
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] and not space_check(board, position):
        position = int(input('Choose your next game position (1-9): '))

    return position


## 6 Ask Player to Play again
def replay():
    choice = input('Play again? Yes or No: ').lower()

    return choice == 'yes'

# Initialize

print(' ••• Welcome to Tic Tac Toe! •••')

while True:

    #PLAY THE GAME
    ## SET UP Board, Marker, Turn 
    myBoard = [' '] * 10
    display_board(myBoard)
    p1_marker, p2_marker = player_input()

    turn = choose_first()
    print(f'{turn} choose first')

    play_game = input('Ready to play? y or n ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## GAME PLAY
    while game_on:

        if turn == 'Player 1':
            ### P1 TURN

            #show board, choose position, place marker
            display_board(myBoard)
            position = player_choice(myBoard)
            place_marker(myBoard, p1_marker, position)

            #Check if win, tie, next player turn
            if win_check(myBoard, p1_marker):
                display_board(myBoard)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(myBoard):
                    display_board(myBoard)
                    print('TIE GAME')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
        ### P2 TURN

            #show board, choose position, place marker
            display_board(myBoard)
            position = player_choice(myBoard)
            place_marker(myBoard, p2_marker, position)

            #Check if win, tie, next player turn
            if win_check(myBoard, p2_marker):
                display_board(myBoard)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(myBoard):
                    display_board(myBoard)
                    print('TIE GAME')
                    game_on = False
                else:
                    turn = 'Player 1'


    if not replay():
        break

    #BREAK OUT OF LOOP ON Replay