class Solution:
    def __init__(self):
        self.compt = {}
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_comp = n
        comp = {}
        for i in range(n):
            comp[i]=set()
            comp[i].add(i)
        for edge in edges:
            find_0 = self.find_comp(comp, edge[0])
            find_1 = self.find_comp(comp, edge[1])
            if find_0 != find_1:
                num_comp -= 1 
                comp[find_0] = comp[find_0].union(comp[find_1])
                comp.pop(find_1) 
        return len(comp.keys())
    
    @staticmethod
    def find_comp(comp, vertex):
        for key, val in comp.items():
            if vertex in val:
                return key
        return None
