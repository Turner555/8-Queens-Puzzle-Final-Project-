_board = ["[]"] * 8

def board(placed, row, column):
    if row == 9:
        return 1
    
    if row in placed:
        for column in range(len(placed)):
            if placed[column] == row:
                _board[column] = " Q"
                print(f"{" ".join(_board)} ")
                _board[column] = "[]"
                break
    else:
        print(" ".join(_board))
    
    board(placed, row + 1, column)

board([1, 0, 3, 0, 5, 0, 7, 0], 1, 0)