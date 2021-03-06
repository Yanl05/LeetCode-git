'''
牛牛以前在老师那里得到了一个正整数数对(x, y), 牛牛忘记他们具体是多少了。
但是牛牛记得老师告诉过他x和y均不大于n, 并且x除以y的余数大于等于k。
牛牛希望你能帮他计算一共有多少个可能的数对。
输入描述:
输入包括两个正整数n,k(1 <= n <= 10^5, 0 <= k <= n - 1)。
输出描述:
对于每个测试用例, 输出一个正整数表示可能的数对数量。
输入例子1:
5 2
输出例子1:
7
例子说明1:
满足条件的数对有(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(5,3)
'''
import sys
line = sys.stdin.readline()
n, k = map(int, line.split())
count = 0
if k == 0:
    count = n * n
else:
    for y in range(k + 1, n + 1):
        count = count + (n // y) * (y - k)  # // 取整
        #  余数为(1， .... ，y-1 ， 0）有n//y 个循环
        if n % y >= k:  # % 求余
            # 余数为(1， .... ，y-1 ）只有1个
            count = count + (n % y - k + 1)  # +1是因为序列n从1开始。
print(count)