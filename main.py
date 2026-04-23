from placement import place_queens
from board import make_board
from input_check import int_check, response_check

def main(placed):
    #Get placement of queen from user
    current_piece = input("What colum and row do you want to place the queen on (ex. 1 3): ")
    
    #Check whether the user inputed column and row correctly
    col_row = int_check(current_piece)
    
    column = (int(col_row[0]) - 1)
    
    row = int(col_row[1])
    
    #Check validity of placement
    result = place_queens(placed, column, row)
    

    #Keep going if placement is valid and there are possible outcomes.
    if result[1] > 0 and result[1] != 100:
        print(f"\n\nYou are on the right track! There are {result[1]} possible solutions left.")
        print("Please place your next queen.")
        #Make a visual board in GUI
        make_board(placed, 1)
        return main(placed)

    #Re-do last placement if there are no more valid solutions.
    elif result[1] == 0:
        print("\n\nOh no! This leads to a dead end.")
        print("Please re-place your last queen.")
        #Make a visual board in GUI
        make_board(placed, 1)
        return main(placed)

    #Re-do last placement if it conflicts with the queens already on the board.
    elif result[1] == -1:
        print("\n\nYikes! THis placement conflicts with queens already on the board")
        print("Please re-place your last queen.")
        #Make a visual board in GUI
        make_board(placed, 1)
        return main(placed)

    #Let user know they completed the puzzle and ask if they want to go again.
    elif result[1] == 100:
        print("\n\nCongrats on finding a way to complete the standoff!")
        #Make a visual board in GUI
        make_board(placed, 1)
        print("\nWould you like to try another route?")
        again = input("y/n: ")
        answer = response_check(again)
        if answer == 'y':
           return main([0, 0, 0, 0, 0, 0, 0, 0])
        elif answer == 'n':
            return -1

#Intro and initial call into the program
print("\nHello, and welcome to The Royal Standoff!\n")
print("To begin, please place your first queen.\n")
board = [0, 0, 0, 0, 0, 0, 0, 0]
#Make a visual board in GUI
make_board(board, 1)
main(board)
