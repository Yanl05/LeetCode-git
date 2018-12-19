class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        需要求的就是a+b=(-c)，然后在余下的链表里做两数相加即可。注意去重！
        """
        # end = []
        # lenn = len(nums)
        # nums.sort()
        # for i in range(lenn-2):
        #     for j in range(i+1, lenn-1):
        #             a = nums[i]
        #             b = nums[j]
        #             if -(a + b) in nums[j+1:lenn]:
        #                 temp = [a, b, (-1) * (a + b)]
        #                 if temp not in end:
        #                     end.append(temp)
        # return end





        # ans = []
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if i == 0 or nums[i] > nums[i-1]:  # nums[i] > nums[i-1] 判断nums[i]与nums[i+1]是否相同
        #         left = i + 1
        #         right = len(nums) - 1
        #         while left < right:
        #             ident = nums[left] + nums[right] + nums[i]
        #             if ident == 0:
        #                 ans.append([nums[i], nums[left], nums[right]])
        #                 left += 1; right -= 1
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right + 1]:
        #                     right -= 1
        #             elif ident < 0:
        #                 left += 1
        #             else:
        #                 right -= 1
        # return ans

        import collections

        diction = collections.Counter(nums)
        print(diction)
        dict_key = diction.keys()
        print(dict_key)

        pos, neg = [], []
        for p in dict_key:
            if p > 0:
                pos.append(p)
            else:
                neg.append(p)

        rsts = []

        if diction.get(0, 0) > 2:  # 如果字典中关键字为0的数量大于2，则添加0，0,0 到返回列表中
            #  dict.get(key, default=None)
            rsts.append(0, 0, 0)
        for p in pos:
            for n in neg:
                inverse = -p - n
                if inverse in dict_key:
                # ensure the third one is the mid one
                    if n < inverse < p:
                        rsts.append([n, inverse, p])
                    elif (inverse == p or inverse == n) and diction[inverse] > 1:
                        rsts.append([n, inverse, p])
        return rsts



print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
