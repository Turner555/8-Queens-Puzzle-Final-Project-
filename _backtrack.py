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

def possible_placements(placed, column, row):
    while row < 10:
        validity = check(placed, column, row)
        if validity == True:
            placed[column] = row
            possible_placements(placed, column + 1, row)
        elif validity == False:
            possible_placements(placed, column, row + 1)

        return placed
        break

def place_queens(placed, current_piece):
    current_piece = input("What colum and row have you placed the queen on (e.g. 1 3): ")
    column = (int(current_piece.split()[0]) - 1)
    row = int(current_piece.split()[1])
    validity = check(placed, column, row)
    if validity is True:
         placed[column] = row
    else:
         print("This placement is not valid")
    # Get a column for the possibility check
    check_for_next = []
    for c in range(len(placed)):
        if placed[c] == 0:
            check_for_next.append(c)
            break
    possible_placements(placed, check_for_next[0])

    return placed

if __name__ == "__main__":
    print(place_queens([0, 0, 0, 0, 0, 0, 0, 0], 0))