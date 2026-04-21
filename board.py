even_row = ["[ ]", "[/]"] * 4
odd_row = ["[/]", "[ ]"] * 4

def make_board(placed, row, col):
    if row == 9:
        return placed
    
    if row == 1:
        print("   1   2   3   4   5   6   7   8 ")
    
    if row in placed:
        for column in range(len(placed)):
            if row % 2 == 0:
                if placed[column] == row:
                    even_row[column] = "[Q]"
                    #Print column and its elements
                    print(f"{row} {' '.join(even_row)}")
                    if column % 2 == 0:
                        even_row[column] = "[ ]"
                    else:
                        even_row[column] = "[/]"
                    break
                
            elif row % 2 != 0:    
                if placed[column] == row:
                    odd_row[column] = "[Q]"
                    #Print column and its elements
                    print(f"{row} {' '.join(odd_row)}")
                    if column % 2 == 0:
                        odd_row[column] = "[/]"
                    else:
                        odd_row[column] = "[ ]"
                    break
    else:
        if row % 2 == 0:
            #Print column and its elements
            print(f"{row} {' '.join(even_row)}")
        else:
            #Print column and its elements
            print(f"{row} {' '.join(odd_row)}")
    
    make_board(placed, row + 1, col + 1)

#Print header for rows

if __name__ == "__main__":
    make_board([1, 0, 3, 0, 5, 0, 7, 0], 1, 0)