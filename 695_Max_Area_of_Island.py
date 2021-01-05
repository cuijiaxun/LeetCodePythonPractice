class Solution:
    # DFS solution
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        shape = (len(grid),len(grid[0]))
        self.visited = [[False for i in range(shape[1])] for j in range(shape[0])]
        self.grid = grid
        self.shape = shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    size = self.dfs(i,j)
                    if size > max_area:
                        max_area = size
        return max_area
            
    
    def dfs(self,i,j):
        self.visited[i][j]= True
        up, down, left, right = 0,0,0,0
        if i-1>=0 and self.visited[i-1][j]==0 and self.grid[i-1][j]==1:
            up = self.dfs( i-1,j)
        if j-1>=0 and self.visited[i][j-1]==0 and self.grid[i][j-1]==1:
            left = self.dfs(  i,j-1)
        if i+1<=self.shape[0]-1 and self.visited[i+1][j]==0 and self.grid[i+1][j]==1:
            down = self.dfs( i+1,j)
        if j+1<=self.shape[1]-1 and self.visited[i][j+1]==0 and self.grid[i][j+1]==1:
            right = self.dfs( i,j+1)
        size = up+left+down+right+1
        return size
