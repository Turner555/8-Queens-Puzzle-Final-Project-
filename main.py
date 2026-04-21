from _backtrack import place_queens
from board import make_board

def main(placed):
    #Get placement of queen from user
    current_piece = input("What colum and row do you want to place the queen on (ex. 1 3): ")
    column = (int(current_piece.split()[0]) - 1)
    #Guard against invalid column.
    if column < 0 or column > 7:
        print("Oops, it looks like this is not a valid column. Please re-enter a column and row between 1 and 8.")
        print(placed)
        return main(placed)
    row = int(current_piece.split()[1])
    #Guard against invalid row.
    if row < 1 or row > 8:
        print("Oops, it looks like this is not a valid row. Please re-enter a column and row between 1 and 8.")
        print(placed)
        return main(placed)

    #Check validity of placement
    result = place_queens(placed, column, row)
    #print(result)

    #Keep going if placement is valid and there are possible outcomes.
    if result[1] > 0 and result[1] != 100:
        print(f"\n\nYou are on the right track! There are {result[1]} possible solutions left.")
        print("Please place your next queen.")
        #Make a visual board in GUI
        make_board(placed, 1, 0)
        return main(placed)

    #Re-do last placement if there are no more valid solutions.
    elif result[1] == 0:
        print("\n\nOh no! This leads to a dead end.")
        print("Please re-place your last queen.")
        #Make a visual board in GUI
        make_board(placed, 1, 0)
        return main(placed)

    #Re-do last placement if it conflicts with the queens already on the board.
    elif result[1] == -1:
        print("\n\nYikes! THis placement conflicts with queens already on the board")
        print("Please re-place your last queen.")
        #Make a visual board in GUI
        make_board(placed, 1, 0)
        return main(placed)

    #Let user know they completed the puzzle and ask if they want to go again.
    elif result[1] == 100:
        print("\n\nCongrats on finding a way to complete the standoff!")
        #Make a visual board in GUI
        make_board(placed, 1, 0)
        print("\nWould you like to try another route?")
        again = input("y/n: ")
        if again == 'y':
           return main([0, 0, 0, 0, 0, 0, 0, 0])
        elif again == 'n':
            return -1

#Intro and initial call into the program
print("Hello, and welcome to The Royal Standoff!\n")
print("To begin, please place your first queen.\n")
board = [0, 0, 0, 0, 0, 0, 0, 0]
#Make a visual board in GUI
make_board(board, 1, 0)
main(board)
