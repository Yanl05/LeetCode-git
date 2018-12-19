class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 61.25%
        # if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        #     return 0
        # ways = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        # # print(ways)
        # for i in range(len(obstacleGrid)):
        #     for j in range(len(obstacleGrid[0])):
        #         if obstacleGrid[i][j] != 1:
        #             if (i == 0 and j == 0) or (j-1>=0 and ways[i][j-1] != 0 and i == 0)  or \
        #                 (i - 1 >= 0 and ways[i-1][j] != 0 and j == 0):
        #             # if i == 0 or j == 0:
        #                 ways[i][j] = 1
        #             else:
        #                 ways[i][j] = ways[i][j-1] + ways[i-1][j]
        #
        #         else:
        #             ways[i][j] = 0
        # return ways[-1][-1]
        # # return ways

        # 100%
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    if i == 0 and j == 0:
                        res[i][j] = 1
                    else:
                        # 把当前路径=左+上 分为两个if
                        if i - 1 >= 0:
                            res[i][j] = res[i][j] + res[i-1][j]
                        if j -1 >= 0:
                            res[i][j] += res[i][j-1]
        return res[-1][-1]

print(Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))