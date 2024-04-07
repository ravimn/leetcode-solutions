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
    print(s.solveNQueens(4))
