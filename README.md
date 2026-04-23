# The Royal Standoff

## Description
The Royal Standoff has been designed to simulate playing the classic 8-queens chess puzzle.
The aim of this puzzle is to place eight queens on a chess board without any of them being able to capture each other. 
This means that no two queens can share the same column, row, or diagonal.
This program allows the user to input the column and row they have placed their queen on and checks the validity of the placement.
Addtionally, the program will help the user know if they are on the right track towards solving the puzzle by recursing through all possible solutions of the puzzle based upon their current placements, and allowing them to re-place a piece if there are no possible solutions left after it is placed.

## How to Run
1. Make sure Python is installed on your computer.
2. Open a terminal.
3. Navigate to the folder.
4. Run the program using: python main.py

## Dependencies
1. Use Python 3.0 or above to run.

2. Ensure that the terminal the code is being run on supports ANSI escape codes for colored output.

3. (No additional libraries needed)

## How to Play
Enter the position of the placed queen when prompted.

The program will run and validate the position and possibilities left.

Repeat until all eight queens are placed in valid positions.

## Example Run

Step 1:

Type python main.py into the terminal:

Step 2:

![alt text](images/Screenshot%202026-04-23%20112411.png) 

After seeing this initial output, the user will type a column and row into the terminal with a space seperating each number.

Step 3:

For example if the user were to type "1 1", the program would then output

![alt text](images/Screenshot%202026-04-23%20112802.png)

The program will tell the user whether that placement was valid and how many possible solutions still remain. If the placement is valid, it will add the queen to the board as seen in the top left of the image.
The program will then ask for another placement and repeat the process of validating moves and adding pieces to the board until all 8 queens have been placed in such a way that none of them can attack each other.

Step 4:

Consider if the user were to try "2 2" on their next input 

![alt text](images/Screenshot%202026-04-23%20112838.png)

This placement conflicts with "1 1" on the diagonal. The program recognizes this conflict and will reject the placement, asking the user to re-place the queen.

Step 5:

Consider if the user tried "2 3" instead

![alt text](images/Screenshot%202026-04-23%20112902.png)

While this placement does not conflict with any pieces already on the board, there are no solutions to the puzzle left based upon the placement. As seen through the board representation, if this is the case, the program will not add the queen to the board and will instead ask the user to choose a different placement.

Final:

Once the user successfully places all 8 queens on the board, the program will congradulate the user and ask if they would like to try another route.

![alt text](images/Screenshot%202026-04-23%20115700.png)

If y is typed into the terminal, the program will restart. If n is typed into the terminal the program will end.