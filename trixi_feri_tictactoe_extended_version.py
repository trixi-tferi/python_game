import random

# show the pattern of our tic tac toe game
pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [' ']*10
board[0] = 'y'
players_move_list = []

def pattern_board():
    print('\n')
    print("\033[91m \033[1mOur game pattern:\033[0m \n")
    print(' ', pattern[0],  '|', pattern[1], '|',  pattern[2])
    print('------------')
    print(' ', pattern[3],  '|', pattern[4], '|',  pattern[5])
    print('------------')
    print(' ', pattern[6], '|',  pattern[7], '|',  pattern[8])

# show the gameboard
def gameboard():
    print(' ', board[1],  '|', board[2], '|',  board[3])
    print('------------')
    print(' ', board[4],  '|', board[5], '|',  board[6])
    print('------------')
    print(' ', board[7], '|',  board[8], '|',  board[9])
    
# which line or diagonal is the winner
def check_line(letter, spot1, spot2, spot3):
    if board[spot1] == letter and board[spot2] == letter and board[spot3] == letter:
        return True

def check_all(letter):
    if check_line(letter, 1, 2, 3): #across1
        return True

    if check_line(letter, 4, 5, 6): #across2
        return True
    
    if check_line(letter, 7, 8, 9): #across3
        return True
    
    if check_line(letter, 1, 4, 7): #down1
        return True
    
    if check_line(letter, 2, 5, 8): #down2
        return True

    if check_line(letter, 3, 6, 9): #down3
        return True
    
    if check_line(letter, 1, 5, 9): #diagonal1
        return True

    if check_line(letter, 3, 5, 7): #diagonal2
        return True
        
def player_move():
    
    player = input("Select your place (1-9): ")
    print('\n')
    player = int(player)
    players_move_list.append(player)
    if board[player] != 'x' and board[player] != 'o':
        board[player] = 'x'   
    else:
        print("\033[91m\033[1mThis spot is taken! Chose another!\033[0m \n")
        player_move()
    if check_all('x') == True:
        gameboard()
        print("\n \033[91m \033[1m*****YOU WIN*****\033[0m \n")
        game_is_playing = False
        if play_again():
            del players_move_list[:]
            main()
        else: 
            quit()   

def player2_move():
    player = input("Select your place (1-9): ")
    print('\n')
    player = int(player)
    if board[player] != 'o' and board[player] != 'x':
        board[player] = 'o'   
    else:
        print("\033[91m\033[1mThis spot is taken! Chose another!\033[0m \n")
        player_move()
    if check_all('o') == True:
        gameboard()
        print("\n \033[91m \033[1m*****Player2 WIN!*****\033[0m \n")
        game_is_playing = False
        if play_again():
            del players_move_list[:]
            main()
        else: 
            quit()   

def computer_move():
    
#first check if the comupter can win next step    
    corners = list(board[1] + board[3] + board[7] + board[9])
    center = list(board[5])
    sides = list(board[2] + board[4] + board[6] + board[8])

    move_list_corner = [1, 3, 7, 9]
    move_list_center = 5
    move_list_side = [2, 4, 6, 8]
    
#first computer should take one of the corners
    if ' ' in corners:
        computer = random.choice(move_list_corner)
        
#then the center, if it is free
    elif ' ' in center:
        computer = move_list_center
        
#last computer should take one of the sides
    elif ' ' in sides:
        computer = random.choice(move_list_side)
        


    if board[computer] != 'o' and board[computer] != 'x':
        board[computer] = 'o'
        players_move_list.append(computer)
    else:
        computer_move()
    if check_all('o') == True:
        gameboard()
        print("\n \033[91m \033[1m*****I WIN*****\033[0m \n")
        game_is_playing = False
        if play_again():
            del players_move_list[:]
            main()
        else: 
            quit()  

def vs_computer():
    try:
        player_move()
        computer_move()
        print(players_move_list)
        gameboard()
    except (ValueError, IndexError):
        print('Wrong input! Add a number between 1 and 9')
    except UnboundLocalError:
        gameboard()
        print("\n \033[91mIt's a tie!\033[0m \n")
        game_is_playing = False
        if play_again():
            del players_move_list[:]
            main()
        else: 
            quit()      

def vs_player2():
    try:
        if ' ' in board[0:9]:
            player_move()
            gameboard()
        if ' ' in board[0:9]:
            player2_move()
            gameboard()
        else:
            print("\n \033[91mIt's a tie!\033[0m \n")
            game_is_playing = False
            if play_again():
                main()
            else: 
                quit()
    except (ValueError, IndexError):
        print('Wrong input! Add a number between 1 and 9')

def play_again():
    global board
    print("Would you like to play again? (y/n): ")
    if input().lower().startswith('y'):
        board = [' '] * 10
        return True
    

def main():
    global board
    global players_move_list
    
    mode = input("\n1 or 2 player mode?: ")
    if mode == '1':
        while True: 
            game_is_playing = True
            while game_is_playing:
                vs_computer()

    if mode == '2':    
        while True: 
            game_is_playing = True
            while game_is_playing:
                vs_player2()
    else:
        print('Choose between 1 or 2 plyaer mode!')   
        main()        

        
print('\n')
print("\033[91mWelcome to the magnificent, awesome, incredible, best madaf*kin \033[1m Tic Tac Toe!",'\033[0m' '\n')            
pattern_board()
main()

        
