class Solution:
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def check(self, x, y, board):
        tmp = board[x][y]
        board[x][y] = '.'
        for row in range(9):
            if board[row][y] == tmp:
                return False
        for col in range(9):
            if board[x][col] == tmp:
                return False
        for row in range(3):
            for col in range(3):
                if board[3*(x // 3) + row][3*(y // 3) + col] == tmp:
                    return False
        board[x][y] = tmp
        return True

    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.check(row, col, board) and self.dfs(board):
                            # print(board)
                            return True
                        board[row][col] = '.'
                    return False
        return True

print(Solution().dfs([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
