"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

Solution
The prototypical backtracking problem is the classical n Queens Problem, first proposed by German chess enthusiast Max Bezzel in 
(under his pseudonym “Schachfreund”) for the standard 8 ⇥ 8 board and by François-Joseph Eustache Lionnet in for the more general n ⇥ n board. 
The problem is to place n queens on an n ⇥ n chessboard, so that no two queens are attacking each other.

For readers not familiar with the rules of chess, this means that no two queens are in the same row, the same column, or the same diagonal.
In a letter written to his friend Heinrich Schumacher in 1850, the eminent mathematician Carl Friedrich Gauss wrote that one could easily confirm 
Franz Nauck’s claim that the Eight Queens problem has 92 solutions by trial and error in a few hours. 
His description Tatonniren comes from the French tâtonner, meaning to feel, grope, or fumble around blindly, as if in the dark.
Gauss’s letter described the following recursive strategy for solving the n-queens problem; the same strategy was described in 1882 
by the French recreational mathematician Édouard Lucas, who attributed the method to Emmanuel Laquière. 
We place queens on the board one row at a time, starting with the top row. 
To place the rth queen, we methodically try all n squares in row r from left to right in a simple for loop. 
If a particular square is attacked by an earlier queen, we ignore that square; otherwise, 
we tentatively place a queen on that square and recursively grope for consistent placements of the queens in later rows.

"""
class Solution:
    def solveNQueens(self, n:int) -> list[list[str]]:
        result = []

        def backtracking(QList:list[int]) -> None:
            row = len(QList)
            if row == n:
                result.append(self.convertQList(QList, n))
            
            for j in range(0, n):
                legal = True
                for i in range(0, row):
                    if QList[i] == j or QList[i] == j + row - i or QList[i] == j - row + i:
                        legal = False
                        break
                if legal:
                    QList.append(j)
                    backtracking(QList)
                    QList.pop()

        backtracking([])
        return result
    
    def convertQList(self, q:list[int], n:int) -> list[str]:
        board = []
        for qIndex in q:
            chess_row = ['.']*n
            chess_row[qIndex] = 'Q'
            board.append("".join(chess_row))
        return board




if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(8))
