class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums ==[]:
        #     return 1

        # nums.sort()
        # if nums[0] >1:
        #     return 1
        # for i in range(len(nums) - 1):
        #     if nums[i] <= 0:
        #         continue
        #     if nums[i + 1] > nums[i] + 1:
        #         return nums[i] + 1
        # return nums[-1] + 1

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums)\
                    and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1




print(Solution().firstMissingPositive([3,4,-1,1]))