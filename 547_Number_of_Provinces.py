class Solution:
    def __init__(self):
        self.visited = None
        self.isConnected = None
        self.shape = None
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected = isConnected
        if len(isConnected) < 1: return 0
        shape = (len(isConnected), len(isConnected[0]))
        self.shape = shape
        self.visited = [0 for j in range(shape[1])] 
        num_province = 0 
        for i in range(shape[0]):
            if self.visited[i] == 0:
                self.dfs(i)
                num_province+=1
        return num_province
    
    def dfs(self,i):
        self.visited[i] = 1
        for col in range(self.shape[1]):
            if self.isConnected[i][col] == 1 and self.visited[col]==0:
                self.dfs(col)
