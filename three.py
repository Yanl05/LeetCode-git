'''
给定一个字符串，找出不含有重复字符的最长子串的长度。
示例：
给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
'''
s = input()

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    longestlenth = 1  # 非空子串的长度最小为1
    substr = ''
    for item in s:
        if item not in substr:
            substr += item
        else:
            if len(substr) > longestlenth:
                longestlenth = len(substr)
            #  把重复的字符添加进去，然后截出出新的substr
            substr += item
            substr = substr[substr.index(item) + 1:]
    if len(substr) > longestlenth:
        longestlenth = len(substr)
    return longestlenth





print(lengthOfLongestSubstring(s))