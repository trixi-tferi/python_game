import random

# show the pattern of our tic tac toe game
pattern = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def pattern_board():
    print('\n')
    print("\033[91m \033[1mOur game pattern:\033[0m \n")
    print(' ', pattern[0],  '|', pattern[1], '|',  pattern[2])
    print('------------')
    print(' ', pattern[3],  '|', pattern[4], '|',  pattern[5])
    print('------------')
    print(' ', pattern[6], '|',  pattern[7], '|',  pattern[8])

# show the gameboard
board = [' '] * 10

def gameboard():
    print(' ', board[0],  '|', board[1], '|',  board[2])
    print('------------')
    print(' ', board[3],  '|', board[4], '|',  board[5])
    print('------------')
    print(' ', board[6], '|',  board[7], '|',  board[8])

# which line or diagonal is the winner
def check_line(letter, spot1, spot2, spot3):
    if board[spot1] == letter and board[spot2] == letter and board[spot3] == letter:
        return True

def check_all(letter):
    if check_line(letter, 0, 1, 2): #across1
        return True

    if check_line(letter, 3, 4, 5): #across2
        return True
    
    if check_line(letter, 6, 7, 8): #across3
        return True
    
    if check_line(letter, 0, 3, 6): #down1
        return True
    
    if check_line(letter, 1, 4, 7): #down2
        return True

    if check_line(letter, 2, 5, 8): #down3
        return True
    
    if check_line(letter, 0, 4, 8): #diagonal1
        return True

    if check_line(letter, 2, 4, 6): #diagonal2
        return True

# we would have liked to do a function for playing again
#....and we're still doing...and doing...and trying to find a solution
 
 # def play_again():
    # print("Would you like to play again? (y/n): ")
    # if input().lower().startswith('y'):
        # the_board = [' '] * 10
        # return main()

# our main function that consists the game itself
def main():
    print('\n')
    print("\033[91mWelcome to the magnificent, awesome, incredible, best modaf*kin \033[1m Tic Tac Toe!",'\033[0m' '\n')
    
    while True:
              
        player = input("Select your place (0-8): ")
        print('\n')
        player = int(player)
           
        if board[player] != 'x' and board[player] != 'o':
            board[player] = 'x'
                
            while True:
                
                random.seed()
                computer = random.randint(0, 8)
                
                if board[computer] != 'o' and board[computer] != 'x':
                    board[computer] = 'o'        
                    break

        else:
            print("\033[91m\033[1mThis spot is taken! Chose another!\033[0m \n")

        print(gameboard())
    
        if check_all('x') == True:
            print("\n \033[91m \033[1m*****YOU WIN*****\033[0m \n")
            # if not play_again():
            break
        elif check_all('o') == True:
            print("\n \033[91m \033[1m*****I WIN*****\033[0m \n")
            # if not play_again():
            break

            
        

pattern_board()
main()
# play_again()
        
