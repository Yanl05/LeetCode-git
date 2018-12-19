class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # if not height:
        #     return 0
        # n = len(height)
        # ret = 0
        # left_max, right_max = [0] * n, [0] * n
        # left_max[0] = height[0]
        # for i in range(1, n):
        #     left_max[i] = max(height[i], left_max[i - 1])
        # right_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(height[i], right_max[i + 1])
        #
        # for i in range(1, n - 1):
        #     tmp = min(left_max[i], right_max[i]) - height[i]
        #     ret += tmp
        # return ret

        if not height:
            return 0
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0

        watersum = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    watersum += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    watersum += rightmax - height[right]
                right -= 1
        return watersum

        # print(type(left_max))

# print(Solution().trap([]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))