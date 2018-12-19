# class Solution:
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         lenn = len(nums)
#         ans = []
#         for i in range(lenn - 3):
#             for j in range(i + 1, lenn - 2):
#                 left = j+1
#                 right = lenn-1
#                 while left < right:
#                     count = nums[i]+nums[j]+nums[left]+nums[right]
#                     if count == target:
#                         if [nums[i], nums[j], nums[left], nums[right]] not in ans:
#                             ans.append([nums[i], nums[j], nums[left], nums[right]])
#                             left += 1
#                             right -= 1
#                         else:
#                             left += 1
#                             right -= 1
#                     elif count < target:
#                         left += 1
#                     else:
#                         right -= 1
#         return ans


class Solution:
    def fourSum(self, nums, target):
        result = []  # 返回结果列表
        N = len(nums)
        if N < 4:
            return result
        nums = sorted(nums) # 先把测试用例排序
        for i in range(N - 3):
            if sum(nums[i:i + 4]) > target or sum(nums[-4:]) < target:
                break
            if nums[i] + sum(nums[-3:]) < target:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target2 = target - nums[i]
            for j in range(i + 1, N - 2):
                if sum(nums[j:j + 3]) > target2 or sum(nums[-3:]) < target2:
                    break
                if nums[j] + sum(nums[-2:]) < target2:
                    continue
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target3 = target2 - nums[j]
                left = j + 1
                right = N - 1
                while (left < right):
                    if nums[left] + nums[right] == target3:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1;

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target3:
                        left += 1
                    else:
                        right -= 1
        return result

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))