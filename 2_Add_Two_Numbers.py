# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 0
        res, head = None, None
        while l1 or l2 or count!=0:
            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0
            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            n_sum = (n1+n2+count) % 10
            count = (n1+n2+count) // 10
            if res is None:
                res = ListNode(n_sum)
                head = res
            else:
                res.next = ListNode(n_sum)
                res = res.next

        return head
