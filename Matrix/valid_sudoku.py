maintainer = 'strivingengineer'
'''
Leetcode 36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the 
following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there 
are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
Approach:
To determine if a 9 x 9 Sudoku board is valid, we need to check whether it follows the three rules given:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
We can start by creating three helper functions to check each of these rules for a given row, column, or sub-box:
Time/Space Complexity: O(1)/O(1)

The time and space complexity of the is_valid_sudoku function is O(1) because the input size is fixed at 81 
cells in a 9 x 9 Sudoku board. The function iterates over each row, column, and sub-box of the board and checks 
if it is valid, but the number of iterations is constant and independent of the input size.

The helper functions is_valid_row, is_valid_column, and is_valid_subbox have a time complexity of O(9) = O(1) 
because they check each cell in a row, column, or sub-box, and there are at most 9 cells in each. The space 
complexity of these functions is also O(1) because they use a set of size at most 9 to keep track of the digits 
in the row, column, or sub-box.

Overall, the time and space complexity of the is_valid_sudoku function and its helper functions are constant, 
making them very efficient for checking the validity of a 9 x 9 Sudoku board.
'''
def is_valid_row(board, row):
    """
    Check if the given row of the Sudoku board is valid.
    """
    nums = set()
    for num in board[row]:
        if num != ".":
            if num in nums:
                return False
            nums.add(num)
    return True

def is_valid_column(board, col):
    """
    Check if the given column of the Sudoku board is valid.
    """
    nums = set()
    for row in range(9):
        num = board[row][col]
        if num != ".":
            if num in nums:
                return False
            nums.add(num)
    return True

def is_valid_subbox(board, row, col):
    """
    Check if the 3x3 sub-box containing the given cell in the Sudoku board is valid.
    """
    nums = set()
    for i in range(3):
        for j in range(3):
            num = board[row+i][col+j]
            if num != ".":
                if num in nums:
                    return False
                nums.add(num)
    return True


def is_valid_sudoku(board):
    """
    Check if the given Sudoku board is valid.
    """
    # Check each row
    for row in range(9):
        if not is_valid_row(board, row):
            return False

    # Check each column
    for col in range(9):
        if not is_valid_column(board, col):
            return False

    # Check each 3x3 sub-box
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not is_valid_subbox(board, row, col):
                return False

    # If all checks pass, the board is valid
    return True


'''
The backtracking algorithm works as follows:

Find an empty cell in the puzzle.
Try all possible values (1-9) for the empty cell.
If a value is found that does not violate any of the rules (i.e., it does not appear in the same row, column, 
or sub-box), move on to the next empty cell and repeat step 2.
If no value is found that works, backtrack to the previous empty cell and try the next possible value.
If all possible values have been tried and none work, backtrack further until a previous empty cell has other 
possible values that have not been tried yet.
Repeat steps 2-5 until the puzzle is solved.
Time/Space Complexity: 
The backtracking algorithm can solve most Sudoku puzzles quickly, but its worst-case time and space complexity are 
exponential, which limits its practical use for large puzzles.
'''


def solve_sudoku(board):
    """
    Solve the Sudoku board using the backtracking algorithm.
    """
    # Find an empty cell in the board
    row, col = find_empty_cell(board)

    # If no empty cell is found, the puzzle is solved
    if row is None:
        return True

    # Try all possible values for the empty cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, str(num)):
            # Fill in the empty cell with the valid value
            board[row][col] = str(num)

            # Recursively solve the puzzle with the new board
            if solve_sudoku(board):
                return True

            # If the recursion fails, backtrack and try the next possible value
            board[row][col] = "."

    # If no valid value works, backtrack further
    return False


def find_empty_cell(board):
    """
    Find an empty cell in the Sudoku board.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                return row, col
    return None, None


def is_valid_move(board, row, col, num):
    """
    Check if filling in the given cell with the given value is valid.
    """
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check sub-box
    sub_row = (row // 3) * 3
    sub_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[sub_row + i][sub_col + j] == num:
                return False

    # If no rule is violated, the move is valid
    return True
