''' test board forma '''
test_board = ['#','','','','','','','','','']
def display_board(board):
    '''
    This is a function that display the board which the marker will be
    placed
    '''
    block1 = '{0:<8} | {1:^8} | {2:>8}'.format(board[7],board[8],board[9])
    block2 = '{0:<8} | {1:^8} | {2:>8}'.format(board[4],board[5],board[6])
    block3 = '{0:<8} | {1:^8} | {2:>8}'.format(board[1],board[2],board[3])
    column = '{0:<8} | {1:^8} | {2:>8}'.format('__','__','__')
    print(block1)
    print(column)
    print(block2)
    print(column)
    print(block3)
def player_input():
    '''
    This is a function that take the play input of the
    corresponding board space
    '''
    choice = 'wrong'
    within_range = False
    while choice.isdigit() is False or within_range is False:
        choice = input('please input a number between (1-9): ')
        if choice.isdigit() is False:
            print('Enter a valid number')
        if choice.isdigit() is True:
            if int(choice) in range(1,10):
                within_range = True
            else:
                print('number exceeded')
                within_range = False
    return int(choice)
def marker():
    '''
    This is a function that make sure the player
    input the correct syntax
    '''
    mark_input = 'wrong'
    while mark_input not in ['X', 'O']:
        mark_input= input("pick a marker 'X' or 'O': " )
        if mark_input not in ['X', 'O']:
            print('Sorry wrong marker was selected')
    return mark_input
def place_marker(board, letter, position):
    '''
    This is a function that take in 3 arguments which is the
    board, player marker and correspondin player position.
    the function place in the letter which correspond to the input
    position on the board

    '''
    if board[position] == '':
        test_board[position] = letter
        return True
    return False
def win_check(board, letter):
    '''
    This is a function that check  for the winner
    '''
    if len(board) <= 10:
        if board[1]  == letter and board[2] ==  letter and board[3] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[4]  == letter and board[5] ==  letter and board[6] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[7]  == letter and board[8] ==  letter and board[9] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[1]  == letter and board[4] ==  letter and board[7] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[2]  == letter and board[5] ==  letter and board[8] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[3]  == letter and board[6] ==  letter and board[9] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[1]  == letter and board[5] ==  letter and board[9] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif board[3]  == letter and board[5] ==  letter and board[7] ==  letter:
            print(f' Congratulations! player with marker {letter} won')
            return True
        elif (board[1] != '' and board[2] != '' and board[3] != ''
            and board[4] != '' and board[5] != '' and board[6] != '' and board[7] != ''
            and board[8] != '' and board[9] != ''):
            x_variable = 0
            o_variable = 0
            for index,tuple in enumerate(board):
                if board[index] == 'X':
                    x_variable +=1
                if board[index] == 'O':
                    o_variable +=1
            if (x_variable > o_variable) or (o_variable > x_variable):
                print('YOU TIED')
                return True
print('Welcome to Tic Tac Toe!')
def gameon_choice():
    '''
    This is a function that request for the player
    choice if he wish to continue
    '''
    choice = 'wrong'
    while choice not in ['YES','NO']:
        choice = input("whould you like to keep playing? YES OR NO: ")
        if choice not in ['YES','NO']:
            print("Sorry, i didn't understand. Please make sure to choose YES OR NO")
    if choice == 'YES':
        return True
    return False
START_GAME = True
GAME_ON  = True
while START_GAME:
    PLAYER1 = ''
    PLAYER2 = ''
    def choose_first():
        '''
        This is a function that determine who to play first
        and assign a marker to it
        '''
        global PLAYER1
        global PLAYER2
        print('you are player 1')
        PLAYER1 = marker()
        if PLAYER1 == 'X':
            PLAYER2 = 'O'
        elif PLAYER1 == 'O':
            PLAYER2 = 'X'
    choose_first()
    display_board(test_board)
    while GAME_ON:
        PLAY1 = True
        PLAY2 = False
        while PLAY1:
            WINNER = win_check(test_board,PLAYER2)
            if WINNER:
                test_board = ['#','','','','','','','','','']
                GAME_ON = gameon_choice()
                if GAME_ON:
                    break
                START_GAME = GAME_ON
                break
            else:
                print('player 1 is playing')
                SPACE_CHECK = place_marker(test_board, PLAYER1, player_input())
                print('\n'*100)
                display_board(test_board)
                if SPACE_CHECK:
                    PLAY1 = False
                    PLAY2 = True
                else:
                    print('positon already taken, choose empty positon')
                    PLAY1 = True
                    PLAY2 = False
        while PLAY2:
            WINNER = win_check(test_board,PLAYER1)
            if WINNER:
                test_board = ['#','','','','','','','','','']
                GAME_ON = gameon_choice()
                if GAME_ON:
                    break
                START_GAME =  GAME_ON
                break
            else:
                print('player 2 is playing')
                SPACE_CHECK = place_marker(test_board, PLAYER2, player_input())
                print('\n'*100)
                display_board(test_board)
                if SPACE_CHECK:
                    PLAY2 = False
                    PLAY1 = True
                else:
                    print('positon already taken, choose empty positon')
                    PLAY2 = True
                    PLAY1 = False
