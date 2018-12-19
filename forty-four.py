class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # # s, p 所在的位置
        # sp = 0
        # pp = 0
        # # match 代表s字符串中匹配*的位置
        # match = 0
        # # star 代表*出现的位置
        # star = -1
        # while sp < len(s):
        #     if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
        #         sp += 1
        #         pp += 1
        #     elif pp < len(p) and p[pp] == '*':
        #         star = pp
        #         match =sp
        #         pp += 1
        #     elif star != -1:
        #         pp = star + 1
        #         match += 1
        #         sp = match
        #     else:
        #         return False
        #
        # while pp < len(p) and p[pp] == '*':
        #     pp += 1
        # return pp == len(p)

        sp = 0
        pp = 0
        match = 0
        star = -1
        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':
                star = pp
                match = sp
                pp += 1
            elif star != -1:
                pp = star + 1
                match += 1
                sp = match
            else:
                return False

        while pp < len(p) and p[pp] == '*':
            pp += 1

        return pp == len(p)


print(Solution().isMatch('adbeb', '*a*b'))
