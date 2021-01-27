"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.result = []
        
    def preorder(self, root: 'Node'):
        if root:
            self.result.append(root.val)
            for child in root.children:
                self.preorder(child)
        return self.result
