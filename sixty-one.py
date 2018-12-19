# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
list1 = (1)
for item in list1:
    if list1.index(item) == 0:
        head = ListNode(item)
        tmp = head
    else:
        tmp.next = ListNode(item)
        tmp = tmp.next
# print(head)

# 方法一：
# 先遍历一次求长度，然后再求模得到真正右移数量
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # tmp = head
        # lenh = 1
        # while tmp.next != None:
        #     tmp = tmp.next
        #     lenh += 1
        # head1, tmp = head, head
        # x = lenh-k
        # while x > 1:
        #     tmp = tmp.next
        #     x -= 1
        # head2 = tmp.next
        # tmp.next = None
        # head2.next = head1
        # return head2

        if head == None or k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        # 计算链表长度
        count = 0
        p = dummy
        while p.next != None:
            p = p.next
            count += 1
        # 形成环形
        p.next = dummy.next
        # 求真实的右移数量
        right = count - k % count
        p = dummy.next
        for i in range(1, right):
            p = p.next
        head = p.next
        p.next = None
        return head


print(Solution().rotateRight(head, 1))