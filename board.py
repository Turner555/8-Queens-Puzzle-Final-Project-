#Split board into even and odd rows
even_row = ["\x1b[48;5;188m   \x1b[0m", "\x1b[48;5;94m   \x1b[0m"] * 4
odd_row = ["\x1b[48;5;94m   \x1b[0m", "\x1b[48;5;188m   \x1b[0m"] * 4

#47-white 44-blue

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
                    if column % 2 == 0:
                        even_row[column] = "\x1b[48;5;188m \x1b[38;5;83mQ \x1b[0m"
                    else:
                        even_row[column] = "\x1b[48;5;94m \x1b[38;5;83mQ \x1b[0m"
                    
                    #Print row and its elements
                    print(f"{row} {' '.join(even_row)}")
                    
                    #Put row back to original
                    if column % 2 == 0:
                        even_row[column] = "\x1b[48;5;188m   \x1b[0m"
                    else:
                        even_row[column] = "\x1b[48;5;94m   \x1b[0m"
                    break

            #If dealing with odd row   
            elif row % 2 != 0:    
                if placed[column] == row:
                    
                    #Place queen on board
                    if column % 2 == 0:
                        odd_row[column] = "\x1b[48;5;94m \x1b[38;5;83mQ \x1b[0m"
                    else:
                        odd_row[column] = "\x1b[48;5;188m \x1b[38;5;83mQ \x1b[0m"
                    
                    #Print column and its elements
                    print(f"{row} {' '.join(odd_row)}")
                    
                    #Put row back to original
                    if column % 2 == 0:
                        odd_row[column] = "\x1b[48;5;94m   \x1b[0m"
                    else:
                        odd_row[column] = "\x1b[48;5;188m   \x1b[0m"
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