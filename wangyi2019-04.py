'''
牛牛去犇犇老师家补课，出门的时候面向北方，但是现在他迷路了。虽然他手里有一张地图，但是他需要知道自己面向哪个方向，请你帮帮他。
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示转方向的次数N(N<=1000)。
接下来的一行包含一个长度为N的字符串，由L和R组成，L表示向左转，R表示向右转。
输出描述:
输出牛牛最后面向的方向，N表示北，S表示南，E表示东，W表示西。
输入例子1:
3
LRR
输出例子1:
E

    北N
西W      东E
    南S
'''

N = int(input("转向次数N："))
S = input("长度为N的字符串：（L表示向左转，R表示向右转）:")
def  direction(var):
    return {
        'NL': 'W',
        'NR': 'E',
        'WL': 'S',
        'WR': 'N',
        'SL': 'E',
        'SR': 'W',
        'EL': 'N',
        'ER': 'S'
    }.get(var, 'error')  # Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
initial = 'N'
for i in S:
    if i == 'L':
        var = initial + i
        initial = direction(var)
    if i == 'R':
        var = initial + i
        initial = direction(var)
print(initial)