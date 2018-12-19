import math
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        x = list(str(x))
        lenx = len(x)
        for i in range(lenx // 2):
            if x[i] != x[lenx - 1 - i]:
                return False
        return True



        # if x < 0:
        #     return False
        # if x == 0:
        #     lenx = 0
        # else:
        #     lenx = int(math.log10(x)) + 1
        # t = lenx // 2
        # for i in range(t):
        #     quo = x // (10 ** (lenx - 1))
        #     rem = x % 10
        #     if quo != rem:
        #         return False
        #     x = x -
        #     lenx = lenx - 1
        #     x =
        #
        # return True



print(Solution().isPalindrome(1000021))