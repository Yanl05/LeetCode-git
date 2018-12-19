class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''
        第一步，根据红色的对角线，找对应位置，互换两个数字的值。
        第二步，对每一行数字，根据中线左右翻转。
        '''
        self.diag = len(matrix[0])
        # step 1:
        for i in range(self.diag):
            for j in range(i, self.diag):
                self.swap_mat1(i, j, matrix)
        print(matrix)
        # step 2
        sym = self.diag // 2
        i = 0
        # # 对称轴不动
        # if self.diag % 2 != 0:
        #     while i < sym:
        #         for j in range(self.diag):
        #             self.swap_mat2(i, j, i, matrix)
        #         i += 1
        # # 对称轴也要交换的情况
        # else:
        #     while i < sym:
        #         for j in range(self.diag):
        #             self.swap_mat2(i, j, i, matrix)
        #         i += 1
        while i < sym:
            for j in range(self.diag):
                self.swap_mat2(j, i, i, matrix)
            i += 1


        print(matrix)
        return self.diag
    def swap_mat1(self, n1, n2, matrix):
        matrix[n1][n2], matrix[n2][n1] = matrix[n2][n1], matrix[n1][n2]
        # return
    def swap_mat2(self, n1, n2, i, matrix):
        matrix[n1][n2], matrix[n1][self.diag - i - 1] = matrix[n1][self.diag - i - 1], matrix[n1][n2]







print(Solution().rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))