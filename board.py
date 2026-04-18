_board = ["[]"] * 8

def board(placed, row):
    if row == 8:
        return 1
    
    for column in range(len(placed)):
        if placed[column] == row:
            _board[column] = "Q"
            print(f"{" ".join(_board)}\n")
            _board[column] = "[]"
        
    board(placed, row + 1)

board([1, 0, 3, 0, 5, 0, 7, 0], 1)