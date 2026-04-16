def check(placed, column, row):
        for i in range(len(placed)):
            #Check what placements are already on the board.
            if placed[i] > 0:

                #Check conflicting rows.
                if placed[i] == row:
                    return False
                
                #Check conflicting columns.
                elif i == column:
                    return False
                
                #Check conflicting diaganols.
                elif abs(i - column) == abs(placed[i] - row):
                    return False
        return True

def possible_placements(placed, column):
    #Base case.
    if column == 8:
        return 1
    
    #Skip columns that have already have a queen in them.
    if placed[column] != 0:
        return possible_placements(placed, column + 1)
    
    #Define a variable to hold posssible outcomes.
    outcomes = 0

    #Loop through all rows
    for row in range(1, 9):
        if check(placed, column, row):
            
            #If a row does not conflict with any other queen, place a queen in that row.
            placed[column] = row
            
            #Move on to the next column and check rows. If you make it all the way, possible_placements will evaluate to 1 due to the base case andthe count of outcomes will increase.
            outcomes += possible_placements(placed, column + 1)
            
            #If there is nowhere to move on to, backtrack and try a different route.
            placed[column] = 0
       
    return outcomes


def place_queens(placed, current_piece):
    current_piece = input("What colum and row have you placed the queen on (e.g. 1 3): ")
    column = (int(current_piece.split()[0]) - 1)
    row = int(current_piece.split()[1])
    
    #Check conflicts between current placement and what is already on the board.
    validity = check(placed, column, row)
    
    #If you can place the queen in the desired spot without conflict, add it to the board.
    if validity is True:
         placed[column] = row
    
    #If the placement conflicts with already placed pieces, don't run the recursion and ask for a different placement.
    else:
         print("This placement is not valid")
    
    #Find the first empty column to start the recursion at.
    check_for_next = []
    for c in range(len(placed)):
        if placed[c] == 0:
            check_for_next.append(c)
            break
    
    #Define total_solutions as the result of the recursion.
    total_solutions = possible_placements(placed, check_for_next[0])

    print(f"Total remaining solutions: {total_solutions}")
    
    return placed

if __name__ == "__main__":
    print(place_queens([0, 0, 0, 0, 0, 0, 0, 0], 0))