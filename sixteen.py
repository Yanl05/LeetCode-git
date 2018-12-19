'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        nums.sort()
        print(nums)

        difmin = 9999999
        ans = 0
        lenn = len(nums)
        for i in range(lenn - 2):
            left = i + 1
            right = lenn - 1
            while left < right:
                count = nums[i] + nums[left] + nums[right] -target

                if count == 0:
                    return target
                else:
                    dif = abs(count)
                    if dif <= difmin:
                        ans = count + target
                        difmin = dif
                    if count + target < target:
                        left += 1
                    else:
                        right -= 1
        return ans





print(Solution().threeSumClosest([-1,2,1,-4], 1))