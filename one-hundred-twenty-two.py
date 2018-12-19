class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pricesSub =[]
        sum = 0
        for i in range(len(prices)-1):
            pricesSub.append(prices[i+1] - prices[i])
        for item in pricesSub:
            if item > 0:
                sum = sum +item
        return sum



print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))