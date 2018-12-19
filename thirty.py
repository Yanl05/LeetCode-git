class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        '''
        输入:
        s = "barfoothefoobarman",
        words = ["foo","bar"]
        输出: [0,9]
        解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
        输出的顺序不重要, [9,0] 也是有效答案。
        '''
        if not s or words == []:
            return []
        lenstr = len(s)
        lenword = len(words[0])
        lensubstr = len(words)*lenword
        times = {}
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        ans = []
        for i in range(min(lenword, lenstr-lensubstr+1)):
            self.findAnswer(i, lenstr, lenword, lensubstr, s, times, ans)
        return ans

    def findAnswer(self, strstart, lenstr, lenword, lensubstr, s, times, ans):
        wordstart = strstart
        curr = {}
        while strstart+lensubstr <= lenstr:
            word = s[wordstart:wordstart+lenword]
            wordstart = wordstart + lenword
            if word not in times:
                strstart = wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word] += 1
                else:
                    curr[word] = 1
                if curr[word] > times[word]:
                    curr[s[strstart:strstart+lenword]] -= 1
                    strstart += lenword
                if wordstart - strstart == lensubstr:
                    ans.append(strstart)



print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))