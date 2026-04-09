def check(placed, column, row):
    for i in range(len(placed)):
        if placed[i] > 0:
            if placed[i] == row:
                return False
            elif i == column:
                return False
            elif abs(i - column) == abs(placed[i] - row):
                return False
    return True
    #placed[column] = row

    #check(placed, current_piece)

current_piece = input("What colum and row have you placed the queen on (e.g. 1 3): ")
column = (int(current_piece.split()[0]) - 1)
row = int(current_piece.split()[1])
print(check([0, 0, 0, 0, 0, 0, 0, 0], column, row))