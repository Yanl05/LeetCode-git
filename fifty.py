class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # tmp = 1
        # if n > 0:
        #     for i in range(n):
        #         tmp = tmp*x
        # elif n == 0:
        #     return 1
        # else:
        #     x = 1 / x
        #     n = abs(n)
        #     for i in range(n):
        #         tmp = tmp*x
        # return tmp
        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            n = abs(n)
            x = 1 / x
        x0 = x * x
        if n % 2 == 0:
            self.res = self.myPow(x0, n//2)
        else:
            self.res = self.myPow(x0, n//2) * x
        return self.res
print(Solution().myPow(2.00000, 10))