# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #Try to solve using bfs
        visited = set()
        clone_dict = {}
        if node is None: return 
        node_stack = [node]
        clone_dict[node.val] = Node(node.val)
        
        while len(node_stack)>0:
            current = node_stack.pop()
            visited.add(current.val)
            neighbours=current.neighbors
            for nb in neighbours:
                if nb.val not in visited:
                    node_stack.append(nb)
                    visited.add(nb.val)
                if nb.val in clone_dict.keys():
                    update_node = clone_dict[nb.val]
                else:
                    update_node = Node(nb.val)
                    clone_dict[nb.val] = update_node
                clone_dict[current.val].neighbors.append(update_node)
            
        
        return clone_dict[1]
        
