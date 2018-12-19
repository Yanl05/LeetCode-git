class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minv = 2**31
        max_d = 0
        for p in prices:
            if p < minv:
                minv = p
            elif p - minv > max_d:
                max_d = p - minv
        return max_d

        # pd = []
        # for i in range(len(prices) - 1):
        #     pd.append(prices[i + 1] - prices[i])
        # max = -(2**31)
        # sum = 0
        # for i in range(len(pd)):
        #     if sum <= 0:
        #         sum = pd[i]
        #     else:
        #         sum = sum + pd[i]
        #     if max < sum:
        #         max = sum
        # if max <= 0:
        #     return 0
        # else:
        #     return max



print(Solution().maxProfit([7,1,5,3,6,4]))
# print(Solution().maxProfit([2, 1]))