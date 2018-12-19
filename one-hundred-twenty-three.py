class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = []
        for i in range(len(prices)):
            tmp1 = prices[:i]
            tmp2 = prices[i:]
            # print(tmp1, tmp2)
            ans1 = self.max(tmp1)
            ans2 = self.max(tmp2)
            ans.append(ans1 + ans2)
            # print(ans)
        ans = sorted(ans)
        # print(ans)
        return ans[-1]
    def max(self, nums):
        minv = 2**31
        max_d = 0
        for n in nums:
            if n < minv:
                minv = n
            elif n - minv > max_d:
                max_d = n - minv
        return max_d





print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))