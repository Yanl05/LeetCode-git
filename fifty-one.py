class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        n 皇后，行，列，对角线上都只能存在一个
        """
        board = [-1 for i in range(n)]
        solution = []
        self.dfs(0, board, [], solution)
        return solution
    def dfs(self, depth, board, valuelist, solution):
        if depth == len(board):
            solution.append(valuelist)
        for row in range(len(board)):
            if self.check(depth, row, board):
                s = '.'*len(board)
                board[depth] = row
                self.dfs(depth+1, board, valuelist+[s[:row]+'Q'+s[row+1:]], solution)

    def check(self, depth, row, board):
        for i in range(depth):
            # 如果两个皇后在同一对角线，那么|row1-row2| = |column1 - column2|
            # if board[i] == row or abs(depth-i) == abs(board[i]-row):
            if board[i] == row or abs(depth - i) == abs(row - board[i]):
                return False
        return True
    #     board = [-1 for i in range(n)]
    #     solution = []
    #     self.dfs(0, board, [], solution)
    #     return solution
    #
    # def dfs(self, depth, board, valuelist, solution):
    #     if depth == len(board):
    #         solution.append(valuelist)
    #     for row in range(len(board)):
    #         if self.check(depth, row, board):
    #             s = '.' * len(board)
    #             board[depth] = row
    #             self.dfs(depth + 1, board, valuelist + [s[:row] + 'Q' + s[row + 1:]], solution)
    #
    # def check(self, k, j, board):
    #     for i in range(k):
    #         if board[i] == j or abs(k - i) == abs(board[i] - j):
    #             return False
    #     return True




print(Solution().solveNQueens(4))