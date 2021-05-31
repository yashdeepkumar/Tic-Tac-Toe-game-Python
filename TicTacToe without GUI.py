import random

# Taking list as input and displaying the board
def display_board(board):
	print("\n"*10)
	print(board[7] + '|' + board[8] + '|' + board[9])
	print("-----")
	print(board[4] + '|' + board[5] + '|' + board[6])
	print("-----")
	print(board[1] + '|' + board[2] + '|' + board[3])

test_board = ['#','X','O','X','O','X','O','X','O',' ']
# display_board(test_board)

# Function to make the player choose between x and o
# 1st iteration of player input function
# def player_input():
# 	player1 = input("Player 1 choose X or O :")
# 	flag = True
# 	while flag:
# 		if player1 == 'x' or player1 == 'X':
# 			print("Player 2 you have no choice but to choose O")
# 			flag = False
# 		elif player1 == 'o' or player1 == 'O':
# 			print("Player 2 you have no choice but to choose X")
# 			flag = False
# 		else:
# 			print("Hey enter a valid input")
# 			flag = False

# 2nd iteration of player input function
def player_input():
	marker = ''
	while not(marker == 'X' or marker == 'O'):
		marker = input("Hey player choose X or O : ").upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

# player1 , player2 = player_input()
# print(player1, player2)

# This function assigns the marker to the desired position
def place_marker(board, marker, position):
	board[position] = marker

# place_marker(test_board, '$', 8)
# display_board(test_board)

# This function is to check whether the board is full or not
def win_check(board, mark):
	return((board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[1] == board[4] == board[7] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	(board[1] == board[5] == board[9] == mark) or
	(board[7] == board[5] == board[3] == mark))

# x = win_check(test_board, 'X')
# print(x)
# display_board(test_board)

# This function is to see who goes first
def choose_first():
	coinflip = random.randint(0, 1)
	if coinflip == 0:
		return 'Player 1'
	else:
		return 'Player 2'

# print(choose_first())

# This function is to see if there is a space in the board
def space_check(board, position):
	return board[position] == ' '

# print(space_check(test_board, 6))

# This function is to check whether the board is full or not
def full_board_check(board):
	count = 0
	for pos in range(1,10):
		if board[pos] != ' ':
			count += 1

	return count == 9

# print(full_board_check(test_board))

# This function is to ask the player's position choice and to see if it is free
def player_choice(board):
	position = 0
	while position not in range(1, 10) or not space_check(board, position):
		position = int(input("Enter the position to be filled : "))
	return position	

# print(palyer_choice(test_board))

# This function is to ask if the players want to play again
def replay():
	play = input("Do you want to play again? Enter Y for yes and N for no : ").upper()
	return play == 'Y'

# print(replay())
print("Let's play Tic-Tac-Toe")
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break