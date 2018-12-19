import re
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        '.' 匹配任意单个字符。
        '*' 匹配零个或多个前面的元素。
        """
        x = (re.match(p, s))
        if x == None:
            return False
        t = x.group()
        if x.group() != s:
            return False
        return True




print(Solution().isMatch("aa", "a"))