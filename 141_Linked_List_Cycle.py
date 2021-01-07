a# Definition for singly-linked list.
'''
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None
        self.visted = False
'''        

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            visited.add(head)
            if head.next is None:
                return False
            elif head.next in visited:
                return True
            else:
                head = head.next
        return False
