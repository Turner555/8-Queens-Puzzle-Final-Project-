#Split board into even and odd rows
even_row = ["[ ]", "[/]"] * 4
odd_row = ["[/]", "[ ]"] * 4

def make_board(placed, row):
    #Base case
    if row == 9:
        return placed
    
    #Column header
    if row == 1:
        print("   1   2   3   4   5   6   7   8 ")
    
    #Print each row and any queens in that row
    if row in placed:
        for column in range(len(placed)):
            
            #If dealing with even rows
            if row % 2 == 0:
                if placed[column] == row:
                    
                    #Place queen on board
                    even_row[column] = "[\x1b[1,31mQ]"
                    
                    #Print row and its elements
                    print(f"{row} {' '.join(even_row)}")
                    
                    #Put row back to original
                    if column % 2 == 0:
                        even_row[column] = "[ ]"
                    else:
                        even_row[column] = "[/]"
                    break

            #If dealing with odd row   
            elif row % 2 != 0:    
                if placed[column] == row:
                    
                    #Place queen on board
                    odd_row[column] = "[Q]"
                    
                    #Print column and its elements
                    print(f"{row} {' '.join(odd_row)}")
                    
                    #Put row back to original
                    if column % 2 == 0:
                        odd_row[column] = "[/]"
                    else:
                        odd_row[column] = "[ ]"
                    break
    
    #If there are no queens in the current row
    else:
        if row % 2 == 0:
            #Print row
            print(f"{row} {' '.join(even_row)}")
        else:
            #Print row
            print(f"{row} {' '.join(odd_row)}")
    
    make_board(placed, row + 1)


if __name__ == "__main__":
    make_board([1, 0, 3, 0, 5, 0, 7, 0], 1)