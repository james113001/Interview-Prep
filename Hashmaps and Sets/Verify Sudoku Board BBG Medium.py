""" Verify Sudoku Board
Medium
Given a partially completed 9×9 Sudoku board, determine if the current state of the board adheres to the rules of the game:

Each row and column must contain unique numbers between 1 and 9, or be empty (represented as 0).

Each of the nine 3×3 subgrids that compose the grid must contain unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the current state of the board is valid given these rules, not whether the board is solvable.

Example:

Output: False
Constraints:
Assume each integer on the board falls in the range of [0, 9].
 """
from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    grids = [set() for _ in range(9)]

    
    
    for rowi, row in enumerate(board):
        for coli, num in enumerate(row):
            if num == 0:
                continue
            
            #rowband* width + colband helps get grid index
            gridi = rowi//3 * 3 + coli//3
            if num in rows[rowi] or num in cols[coli] or num in grids[gridi]:
                return False
            
            rows[rowi].add(num)
            cols[coli].add(num)
            grids[gridi].add(num)
    return True        
    #O Complexity: O(1) since the board size is fixed at 9x9, the time complexity is constant. 
    # The space complexity is also O(1) as we are using a fixed amount of additional space for 
    # the sets to track the numbers in rows, columns, and grids.