import math
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        '''
        sym = 1
        if dividend > 0 and divisor < 0 or dividend <0 and divisor > 0:
            sym = -1
        dig1 = math.fabs(dividend)
        dig2 = math.fabs(divisor)
        while dig1 == dig2:
            return sym
        if dig2 == 1:
            return sym*dig1
        t = dig2
        p = 1
        ret = 0
        while t < dig1:
            ret = ret + p
            t = 2*t
            p = 2*p
        ret = ret - p/4
        dig3 = dig1 - t/2
        t = dig2
        p = 1
        while t < dig3:
            ret = ret + p
            t =2*t
            p = 2*p
        ret = ret - p/2



        if ret < -2**31 or ret > 2**31-1:
            return 2**31-1
        return int(ret*sym)
        '''

        '''
        MAX_INT = 2147483647

        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1

        quotient = 0

        dividend = abs(dividend)

        divisor = abs(divisor)

        while dividend >= divisor:

            k = 0

            tmp = divisor

            while dividend >= tmp:
                dividend -= tmp

                quotient += 1 << k

                tmp <<= 1

                k += 1

        quotient = sign * quotient

        if quotient > MAX_INT:
            quotient = MAX_INT

        return quotient
        '''

        #MAX_INT = 2147483647
        sign = -1 if (dividend<0 and divisor>0) or (dividend>0 and divisor<0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                #dig = 1 << k
                ret += 1 << k
                tmp <<= 1
                k += 1


        ret = ret*sign
        ret = 2**31-1 if ret<=-2**31 or ret>=2**31-1 else ret
        return ret
#print(Solution().divide(-2147483648, 2))
print(Solution().divide(7, -3))