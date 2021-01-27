class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        new_root = Node(val=root.val, children=None)
        for child in root.children:
            new_root.children.append(self.cloneTree(child))
        return new_root
