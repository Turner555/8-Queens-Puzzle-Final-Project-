from _backtrack import place_queens

def main(placed):
    #Get placement of queen from user
    current_piece = input("What colum and row have you placed the queen on (e.g. 1 3): ")
    column = (int(current_piece.split()[0]) - 1)
    row = int(current_piece.split()[1])
    
    #Check validity of placement
    result = place_queens(placed, column, row)
    print(result)

    #Keep going if placement is valid and there are possible outcomes.
    if result[1] > 0 and result[1] != 100:
        print(f"You are on the right track. There are {result[1]} possible solutions left.")
        print("Please place your next queen.")
        main(placed)

    #Re-do last placement if there are no more valid solutions.
    elif result[1] == 0:
        print("Oh no! This leads to a dead end.")
        print("Please re-place your last queen.")
        main(placed)

    #Re-do last placement if it conflicts with the queens already on the board.
    elif result[1] == -1:
        print("Yikes! THis placement conflicts with queens already on the board")
        print("Please re-place your last queen.")
        main(placed)

    #Let user know they completed the puzzle and ask if they want to go again.
    elif result[1] == 100:
        print("Congrats on finding a way to complete the standoff!")
        print("Would you like to try another route.")
        again = input("y/n: ")
        if again == 'y':
            main([0, 0, 0, 0, 0, 0, 0, 0])
        elif again == 'n':
            return -1

#Intro and initial call into the program
print("Hello, and welcome to The Royal Standoff!")
print("To begin, please place your first queen.")
board = [0, 0, 0, 0, 0, 0, 0, 0]
main(board)