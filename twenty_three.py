# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        a为普通列表 
        - heapq.heapify(a) 调整a，使得其满足最小堆 
        - heapq.heappop(a) 从最小堆中弹出最小的元素 
        - heapq.heappush(a,b) 向最小堆中压入新的元素
        '''

        class Solution:
            def mergeKLists(self, lists):
                """
                :type lists: List[ListNode]
                :rtype: ListNode
                """
                res = []
                for i in lists:
                    while i:
                        res.append(i.val)
                        i = i.next
                if res == []:
                    return []
                print(res)
                res.sort()
                print(res)
                l = ListNode(0)
                first = l
                while res:
                    l.next = ListNode(res.pop(0))
                    l = l.next
                return first.next


