class Solution:
    def __init__(self):
        self.grid = None
        self.visited = None
        self.shape = None
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if len(grid) == 0: return 0
        shape = (len(grid), len(grid[0]))
        self.shape = shape
        self.visited = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
        num_island = 0
        for i in range(shape[0]):
            for j in range(shape[1]):
                if grid[i][j] == '1' and self.visited[i][j] == 0:
                    self.dfs(i,j)
                    num_island +=1
        return num_island
        
    def dfs(self, i, j):
        self.visited[i][j] = 1
        if i>0 and self.grid[i-1][j] == '1' and self.visited[i-1][j] == 0:
            self.dfs(i-1,j)
        if i<self.shape[0]-1 and self.grid[i+1][j] == '1' and self.visited[i+1][j] == 0:
            self.dfs(i+1,j)
        if j>0 and self.grid[i][j-1] == '1' and self.visited[i][j-1] == 0:
            self.dfs(i,j-1)
        if j<self.shape[1]-1 and self.grid[i][j+1] == '1' and self.visited[i][j+1] == 0:
            self.dfs(i,j+1)
