class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.re = []
        self.matrix = matrix
        self.row = len(matrix)
        self.column = len(matrix[0])
        if self.row == 0:
            return []
        self.cyc(self.row, self.column, 0, 0, 0)
        return self.re
    """row记录下一次行数，column记录下一次列数，
    ri记录下一次开始行，ci记录下一次开始列"""
    def cyc(self, row, column, ri, ci, case):
        if row == 0 or column == 0:
            return
        if case == 0:
            endci = ci + column
            for i in range(ci, endci):
                self.re.append(self.matrix[ri][i])
            row = row - 1
            ri = ri + 1
            ci = endci - 1
            case = (case + 1) % 4
            self.cyc(row, column, ri, ci, case)
        elif case == 1:
            endri = ri + row
            for i in range(ri, endri):
                self.re.append(self.matrix[i][ci])
            column = column - 1
            ri = endri - 1
            ci = ci - 1
            case = (case + 1) % 4
            self.cyc(row, column, ri, ci, case)
        elif case == 2:
            for i in range(ci, ci-column, -1):
                self.re.append(self.matrix[ri][i])
            row = row - 1
            ri = ri - 1
            ci = ci - column + 1
            case = (case + 1) % 4
            self.cyc(row, column, ri, ci, case)
        elif case == 3:
            for i in range(ri, ri-row, -1):
                self.re.append(self.matrix[i][ci])
            column = column - 1
            ri = ri-row+1
            ci = ci + 1
            case = (case + 1) % 4
            self.cyc(row, column, ri, ci, case)

print(Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))