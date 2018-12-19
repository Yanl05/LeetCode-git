class Solution:
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     self.res = []
    #     sub = []
    #     self.dfs(nums, sub)
    #     return self.res
    # def dfs(self, Nums, subList):
    #     if len(subList) == len(Nums):
    #         print(self.res, subList)
    #         self.res.append(subList[:])
    #     for m in Nums:
    #         if m in subList:
    #             continue
    #         subList.append(m)
    #         self.dfs(Nums, subList)
    #         subList.remove(m)

    def permute(self, nums):
        self.res = []
        subList = []
        self.dfs(nums, subList)
        return self.res
    def dfs(self, nums, subList):
        if len(nums) == len(subList):
            # print(self.res, subList)
            self.res.append(subList[:])
        for i in nums:
            if i in subList:
                continue
            subList.append(i)
            self.dfs(nums, subList)
            subList.remove(i)

print(Solution().permute([1, 2, 3]))