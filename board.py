_board = ["[ ]"] * 8

def make_board(placed, row, column):
    if row == 9:
        return placed
    
    if row in placed:
        for column in range(len(placed)):
            if placed[column] == row:
                _board[column] = "[Q]"
                print(f"{" ".join(_board)} ")
                _board[column] = "[ ]"
                break
    else:
        print(" ".join(_board))
    
    make_board(placed, row + 1, column)

if __name__ == "__main__":
    make_board([1, 0, 3, 0, 5, 0, 7, 0], 1, 0)