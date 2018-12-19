class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # if num1 == '0' or num2 == '0':
        #     return '0'
        # num1 = num1[::-1]
        # num2 = num2[::-1]
        # retstr = ''
        # ret = [0] * (len(num1) + len(num2))
        # # for i in range(len(num1) - 1, -1, -1):
        # #     for j in range(len(num2) - 1, -1, -1):
        # for i in range(len(num1)):
        #     for j in range(len(num2)):
        #         tmp = int(num1[i]) * int(num2[j])
        #         if not ret[i + j]:
        #             ret[i + j] = tmp
        #         else:
        #             ret[i + j] += tmp
        # for i in range(len(ret)):
        #     # print(ret[i])
        #     if ret[i] >= 10:
        #         ret[i], ret[i + 1] = ret[i] % 10, ret[i + 1] + ret[i] // 10
        #     retstr += str(ret[i])
        # retstr = retstr[::-1]
        # if retstr[0] == '0':
        #     retstr = retstr[1::]
        # # print(type(retstr[0]))
        #
        #
        # return retstr

        if not num1 or not num2:
            return 0
        l1 = len(num1)
        l2 = len(num2)
        return str(int(num1) * int(num2))
        n1 = 0
        for i in range(l1):
            n1 = n1 + int(num1[i]) * 10 ** (l1 - i - 1)
        n2 = 0
        for i in range(l2):
            n2 = n2 + int(num2[i]) * 10 ** (l2 - i - 1)
        return str(n1 * n2)




if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply('12', '5'))