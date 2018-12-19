import List
head = List.Creatlist([1, 2, 3, 4, 5])



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # if head is None:
        #     return None
        #
        # dummy = ListNode(0)
        # dummy.next = head
        #
        # pre = dummy
        # while head:
        #     if head.next:
        #         pre.next = head.next
        #         head.next.next, head.next = head, head.next.next
        #         pre, head = head, head.next
        #     else:
        #         head = None
        #
        # return dummy.next
        '''
        1、建立空的新链表list1.
        2、如果原链表剩余元素个数不小于K个，则取K个元素，采用头插法构建反序的临时链表，插入list1的尾部。
        3、如果链表剩余元素个数小于K个，则将剩余的链表插入到list1的尾部。
        '''

        def reverseList(head, k):
            pre = None
            cur = head
            while cur and k > 0:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                k -= 1
            head.next = cur
            return cur, pre

        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        #print(length)
        if length < k:
            return head
        step = length // k
        ret = None  # ret 返回结果
        pre = None
        p = head
        while p and step:
            next, newHead = reverseList(p, k)
            if ret is None:
                ret = newHead
            if pre:
                pre.next = newHead
            pre = p
            p = next
            step -= 1
        return ret


end = Solution().reverseKGroup(head, 3)
while end:
    print(end.val)
    end = end.next