class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reverse(), 反转列表中的元素

        max = 0
        maxsum = {'maxsum':''}
        lens =len(s)
        if lens == 0:
            return s
        if lens == 1:
            return s

        for i in range(lens):
            s1 = s[i]
            if len(s1)>len(maxsum['maxsum']):
                maxsum['maxsum'] = s1

            for j in range(i+1, lens):
                s1 = s1 + s[j]

                if s1 == s1[::-1]:
                    count = j + 1 - i
                    if max <count:
                        max = count
                        maxsum['maxsum']=s[i:j+1]
                j += 1
        return maxsum['maxsum']


        # mx = 0  # mx即为当前计算回文串最右边字符的最大值
        # ans = 0  # 最大回文数长度
        # po = 0
        # Len = [0] * 10000

        # ##转换字符串
        # def INIT(s):
        #     init_s = '@#'
        #     for x in s:
        #         init_s = init_s + x + '#'
        #     print(init_s)
        #
        #     return init_s + '$', 2 * len(s) + 1  # 字符串结尾加一个字符，防止越界
        #
        # init_s, len_s = INIT(s)  # 转换字符串
        # get_po = 0
        # for i in range(1, len_s):
        #     if mx > i:
        #         Len[i] = min(mx - i, Len[2 * po - i])  # 在Len[j]和mx-i 中取小
        #     else:
        #         Len[i] = 1  # 如果i>mx，要从头开始匹配
        #
        #     while init_s[i - Len[i]] == init_s[i + Len[i]]:
        #         Len[i] = Len[i] + 1
        #
        #     if Len[i] + i > mx:  # 若新计算的回文串右端点位置大于mx，要更新po和mx的值
        #         mx = Len[i] + i
        #         po = i
        #
        #     if ans < Len[i]:
        #         ans = Len[i]
        #         get_po = i
        #
        # return 'ans=  ' + str(ans - 1) + '  get_po= ' + init_s[get_po - ans + 2:get_po + ans:2]  # 返回Len[i]中的最大值-1即为原串的最长回文子串额长度
        #

if __name__ == "__main__":
    print(Solution().longestPalindrome("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"))
    #Solution().longestPalindrome("babad")