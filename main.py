from _backtrack import place_queens

def placement(placed, column, row):
    result = place_queens(placed, column, row)
    return result

def main(placed):
    current_piece = input("What colum and row have you placed the queen on (e.g. 1 3): ")
    column = (int(current_piece.split()[0]) - 1)
    row = int(current_piece.split()[1])
    result = placement(placed, column, row)
    print(result)
    if result[1] > 0 and result[1] != 100:
        print("You are on the right track")
        main(placed)

    elif result[1] == 0:
        print("Uh oh! dead end")
        main(placed)

    elif result[1] == -1:
        print("Conflicts with board")
        main(placed)

    elif result[1] == 100:
        print("You won!")


print("Hello, and welcome to The Royal Standoff!")
print("To begin, please place your first queen.")
board = [0, 0, 0, 0, 0, 0, 0, 0]
main(board)