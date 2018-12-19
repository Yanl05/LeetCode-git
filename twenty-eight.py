class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1
        '''
        if needle == None:
            return 0
        lenh = len(haystack)
        lenn = len(needle)
        for i in range(lenh-lenn+1):
            if haystack[i:i+lenn] == needle:
                return i
        return -1


print(Solution().strStr("Hello", "ll"))