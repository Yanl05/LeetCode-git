# import tensorflow as tf
# dic = {'a': 1, 'b': 2}
# def Func(a, b):
#     print(a + b)
#     return
#
# Func(**dic)
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# evens = [x for x in numbers if x % 2 is 0]
# odds = [y for y in numbers if y not in evens]
# cities = ['London', 'Doblin', 'Oslo']
# def visit(city):
#     print("Welcome to " + city)
# for city in cities:
#     visit(city)
#
# print(odds)
#
# print(evens)
#
# x = [1, 2, 3]
# y = map(lambda x: x + 1, x)
# print(list(y))
# print(type(y))
# for item in y:
#     print(item)
# y = lambda x: x +1;
# print(y(5))
#
# import requests
# import pprint
# url = ' http://www.baidu.com'
# users = requests.get(url).json()
#
# pprint.pprint(users)
#
# keys = ['a', 'b', 'c']
# vals = [1, 2, 3]
# zipped = zip(keys, vals)
# for zip in zipped:
#     print(zip)
# print(zipped)
#
# nums = [5, 4, 7, 5, 3, 2]
# a = nums[5:1:-1]
# b = nums[0:2]
# print(a)
# print(b)
# c = b +a
# print(c)
# print(nums)
#
# import math
# nums = [5, 4, 7, 5, 3, 2]
# def resv3(li):
#     hcnt = int(math.floor(len(li)/2))
#     tmp = 0
#     for i in range(hcnt):
#         tmp = li[i]
#         li[i] = li[-(i+1)]
#         li[-(i+1)] = tmp
#     return li
# print(resv3(nums[2:6]))
# print(nums)
#
# import math
# class Solution:
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums) - 1
#         while (i > 0) and (nums[i - 1] >= nums[i]):
#             i -= 1
#         temp = nums[i - 1]
#         j = i
#         while (j < len(nums)) and (nums[j] > temp):
#             j += 1
#         nums[i - 1] = nums[j - 1]
#         nums[j - 1] = temp
#         nums_part_sorted = sorted(nums[i:])
#         nums[i:] = nums_part_sorted
#         return nums
#
# print(Solution().nextPermutation([3,2,1]))
#
# nums = [1, 2, 5, 4, 3]
# nums_part = sorted(nums[2:])
# nums[2:] = nums_part
# print(nums[2:])
# print(nums_part, nums)
#
# stack = ['(',')', '(']
# i= 3
# print(i-stack[-1])
#
# nums = [4,5,6,7,0,1,2]
# print(nums[6:])

# n = -2
# n = abs(n)
# print(n)

# for j in range(3, 0, -1):
#     print(j)

s = '123'
print(type(s))
print(type(s[1]))
if s[1] > '0':

    print(s[1])