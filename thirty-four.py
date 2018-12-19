class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lenn = len(nums)
        # if lenn == 0:
        #     return [-1, -1]
        # low = 0
        # high = lenn - 1
        # ret = [-1, -1]
        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] < target:
        #         low = mid + 1
        #         continue
        #     elif nums[mid] > target:
        #         high = mid - 1
        #         continue
        #     elif nums[mid] == target:
        #         ret = [mid, mid]
        #         i = 1
        #         while mid - i >= 0:
        #             while nums[mid - i] == target:
        #                 ret[0] = mid - i
        #                 i += 1
        #                 if mid - i < 0:
        #                     break
        #         i = 1
        #         while mid + i > lenn:
        #             while nums[mid + i] == target:
        #                 ret[1] = mid + i
        #                 i += 1
        #                 if mid + i > lenn:
        #                     break
        #         return ret
        # return ret

        length = len(nums)
        l = 0
        r = length - 1
        mid = 0
        res = [-1, -1]
        while l <= r:
            # >> 右移， >>1 代表除以2
            mid = (l + r) >> 1
            if nums[mid] == target: break
            elif nums[mid] > target: r = mid - 1
            else: l = mid + 1
        if l <= r:
            l = mid - 1
            while l >= 0 and nums[l] == nums[mid]: l -= 1
            r = mid + 1
            while r < length and nums[r] == nums[mid]: r += 1
            res[0] = l + 1; res[1] = r - 1
        return res



print(Solution().searchRange([5,7,7,8,8,10], 8))
#print(Solution().searchRange([1], 1))
