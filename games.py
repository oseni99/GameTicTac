# TicTacToe
# the board of the game 

from os import system 
def display_board(board):
    system("cls")
    print(board[1] + "|" + board[2] +"|" + board[3] + "|")
    
    print(board[4] + "|" + board[5] +"|" + board[6] + "|")
    
    print(board[7] + "|" + board[8] +"|" + board[9] + "|")
test_values = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_values)
# players input 

def player_input():
    i = ""
    a = ""
    while i != "X" and i!= "O":
        i = input("Player1 should select (X or 0)").capitalize()
        player1 = i
        player2 = a 
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return(player1,player2)
    
player_input()
# putting markers into the board index 

def place_mark(board,mark,position):
    board[position] = mark
place_mark(test_values,"#",7)
display_board(test_values)

# to check if the mark x or o has won 
def win_check(board,mark):
    return ( (board[1] == board[2] == board[3] == mark) or 
    (board[4] == board[5]== board[6] == mark) or
    (board[7]== board[8] == board[9] == mark) or 
    (board[1] == board[4] == board[7] == mark) or 
    (board[3] == board[6]== board[9]== mark) or 
    (board[1] == board[5] == board[9] == mark) or 
    (board[3] == board[5] == board[7] == mark) or 
    (board[2] == board[5] == board[8] == mark))   
print(win_check(test_values,"X"))
display_board(test_values)

#checking to see randomly which player goes first

from random import randint 

def random_pick():
    rands = randint(1,2)
    if rands == 1:
        print("Player 1")
    else:
        print("Player 2")
random_pick()

# returning a boolean to know whether space is freely availaible on the board 

def space_check(board,position):
    if board[position] == " ":
        return True
    else:
        return False 

# to check if the board is full 

def full_board_check(board):
    for x in range(1,10):
        if space_check(board,x):
            return False
    return True 

# asking for the players next position and if free and return the position 

def player_choice(board):
    position = 0 
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a number from (1-9): "))
    return position 

# asking player if they want to play again  

def replay_game():
    i = ""
    while i != "Y" or i != "N":
        i = input("select your choice of whether(Y or N)").capitalize()
    if i == "Y":
        return True 
    else:
        return False 
    

# RUNNING THE GAME ITSELF 
#while loop to keep the game running.. 
print("Welcome Oluwatosin Tic-Tac-Toe game")

while True:

    #play the game 

    # setting the game up: displaying the board, choosing who plays first, x or o 
    the_board= ["   "]* 10 
    player1,player2 = player_input()
    turn = random_pick()
    play_now = input("Are you ready to play the game? choose (Y or N)").capitalize()
    if play_now == "Y":
        game_on = True 
    else:
        game_on = False 
    #the gameplay 
    while game_on:

        if turn == "Player 1":
            #show the board 
            display_board(the_board)
            #choose a position 
            position = player_choice(the_board)
            # placing x or o  on the position 
            place_mark(the_board,player1,position)
            #check if its won 
            if win_check(the_board,player1):
                display_board(the_board)
                print("PLAYER 1 HAS WON!")
                break 
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break 
                else:
                    turn = "Player 2"
             
        else:
            #show the board 
            display_board(the_board)
            #choose a position 
            position = player_choice(the_board)
            # placing x or o  on the position 
            place_mark(the_board,player2,position)
            #check if its won 
            if win_check(the_board,player2):
                display_board(the_board)
                print("PLAYER 2 HAS WON!")
                break 
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break 
                else:
                    turn = "Player 1"
    if not replay_game():
        break
# BREAKING OUT OF THE LOOP WHEN IT REPLAYS 
