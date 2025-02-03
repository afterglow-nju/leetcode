class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==0:
                return 0
            t=grid[x][y]
            grid[x][y]=0
            return t+bfs(x-1,y)+bfs(x,y-1)+bfs(x+1,y)+bfs(x,y+1)
        
        ret=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret=max(ret,bfs(i,j))
        return ret