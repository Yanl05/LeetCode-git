class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lenn = len(nums)
        # max= -(2**31)
        # sum = 0
        # for i in range(lenn):
        #     if sum <= 0:
        #         sum = nums[i]
        #     else:
        #         sum = sum + nums[i]
        #     if max < sum:
        #         max = sum
        # return max

        lenn =len(nums)
        max = -(2**31)
        sum = 0
        for i in range(lenn):
            if sum <= 0:
                sum = nums[i]
            else:
                sum = sum + nums[i]
            if max < sum:
                max = sum
        return max

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))