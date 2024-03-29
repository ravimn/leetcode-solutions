"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

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
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if self.isValidsudokuRows(board):
            if self.isValidSudokuColumn(board):
                return self.isValidSudokuSquare(board)
        return False
    
    def isValidsudokuRows(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.isValidSudokuList(row):
                return False
        return True
    
    def isValidSudokuColumn(self, board:list[list[str]]) -> bool:
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not self.isValidSudokuList(col):
                return False
        return True
    
    def isValidSudokuSquare(self, board: list[list[str]]) -> bool:
        sboard:list[list[str]] = []
        for i in range(9):
            sboard.append([])
        for i in range(9):
            for j in range(9):
                idx_x = i // 3
                idx_y = j // 3
                idx = idx_x * 3 + idx_y
                sboard[idx].append(board[i][j])
        return self.isValidsudokuRows(sboard)

    def isValidSudokuList(self, nums:list[str]) -> bool:
        numsMap = {}
        for i in nums:
            if i == ".":
                continue
            if i in numsMap:
                return False
            numsMap[i] = 1
        return True
