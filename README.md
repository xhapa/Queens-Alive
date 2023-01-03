# Queens-Alive

## About the problem
It's project that implement a user interface for solving the N-Queens problem. The N-Queens problem is a classic problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens are attacking each other.

<p align="center">
  <img  src="https://i.imgur.com/H9VTHt9.png" width="350" height="245" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img  src="https://i.imgur.com/40mue7Y.png" width="350" height="245" />
</p>

## How does it work?
### Main script
Script defines the ```draw_screen``` function, which is responsible for drawing the user interface on the screen. The function takes three arguments: the board object, which represents the current state of the chessboard, and the ```start_button```, ```more_queens_button```, and ```less_queens_button``` rectangles, which represent the buttons on the screen for starting the solving process, adding more queens to the board, and removing queens from the board, respectively.

The main function is where the bulk of the script's logic resides. It initializes Pygame, sets up the screen, creates the board object, and starts a loop that listens for events, such as mouse clicks on the buttons. When a button is clicked, the appropriate action is performed, such as calling the solve method on the board object to solve the N-Queens problem, or modifying the number of queens on the board. The draw_screen function is called at the end of each iteration of the loop to redraw the user interface on the screen.

In summary, the code above is a Pygame-based implementation of the N-Queens problem with a user interface for solving and visualizing the problem.
### Board Class
The Board class which can be used to create a board for the N-Queens problem. The Board class has several methods that are used to interact with the board and perform operations on it.

The ```__init__``` method is the constructor of the Board class. It takes in an integer N as an argument, which represents the number of rows and columns in the board. The method sets the size of the board to be a square with a width and height of 400 pixels. It also initializes an N x N matrix with all elements set to 0. The block_size attribute of the Board instance is set to the width of the board divided by the number of rows and columns.

The ```draw_board``` method takes in the screen on which the board is to be drawn and the queen image that is to be placed on the board. It uses the draw_grid method to draw the grid on the screen.

The ```draw_grid``` method draws the grid on the screen. It loops through the rows and columns of the N x N matrix, and draws a rectangle on the screen at the corresponding position. The color of the rectangle depends on whether the row and column indices sum to an even or odd number. The method also checks if there is a queen at the current position in the matrix, and if there is, it blits the queen image on the screen at the corresponding position.

The ```reset_board``` method takes in an integer n as an argument, and increases the size of the board by n rows and columns. It resets the matrix to be an (N+n) x (N+n) matrix with all elements set to 0, and updates the block_size attribute of the Board instance accordingly.

#### About the solution
The solve method takes in the row number as an argument and is used to solve the N-Queens problem for the board. It uses a recursive approach to find a solution for the problem. The method first checks if all rows have been considered, in which case it returns True as this means a solution has been found. If not, it loops through all columns in the current row and checks if a queen can be placed at the current position using the ```bounding_func``` method. If a queen can be placed, the method sets the element in the matrix at the current position to 1 and recursively calls itself for the next row. If the recursive call returns True, the method returns True as this means a solution has been found. If not, the element in the matrix at the current position is set back to 0 and the method continues looping through the columns in the current row. If the method has looped through all columns in the current row and no solution has been found, it returns False.

The ```bounding_func``` method takes in the row and column indices as arguments and is used to check if a queen can be placed at the given position. It first checks if there is already a queen in the current row or column. If there is, the method returns False. It then loops through the matrix and checks if there is a queen on any of the diagonals from the current position. If there is, the method returns False. If none of the above conditions are satisfied, the method returns True indicating that a queen can be placed at the given position.
