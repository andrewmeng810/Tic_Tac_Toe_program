


from IPython.display import clear_output



def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')




def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('X', 'O')


def place_marker(board, marker, position):
#     if space_check(board, position):
    board[position] = marker



def win_check(board, mark):
    """ win the game? """
    # all rows, all columns, 2 diagonals
    return ((board[9] == board[8] == board[7] == mark) or
           (board[6] == board[5] == board[4] == mark) or
           (board[3] == board[2] == board[1] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[7] == board[5] == board[3] == mark) or
           (board[1] == board[5] == board[9] == mark))




import numpy as np

def choose_first():
    score1,score2 = np.random.randint(0, 100, size=2)
    if score1 > score2:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return (board[position] == ' ')

# In[140]:


def full_board_check(board):
    for item in range(0,10):
        if space_check(board,item):
            return False
        return True



def player_choice(board):
    position = 0
    while position not in range(1,11) or not space_check(board, position):
        position = int(input('please input desire posistion (1-9): '))
        return position




def replay():
    choice = input ('Do you want to play again? y/n')
    if choice == 'y':
        return True





print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    #pass
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y/n ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False



    while game_on:
        #Player 1 Turn
        if turn == 'player1':
        # show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker on the posistion
            place_marker(the_board, player1_marker, position)

            # check if they won, or a tie
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player1 has won!!!')
                game_on = False

            # no win, tie, the next player's turn
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!!!')
                    game_on = False
                    break
                else:
                    turn = 'player2'

        else:
        # Player2's turn.

            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker on the posistion
            place_marker(the_board, player2_marker, position)

            # check if they won, or a tie
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player2 has won!!!')
                game_on = False

            # no win, tie, the next player's turn
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!!!')
                    game_on = False
                    break
                else:
                    turn = 'player1'



    if not replay():
        break
