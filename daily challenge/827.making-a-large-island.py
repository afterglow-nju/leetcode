class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        q=[]
        area=[]
        def bfs(x,y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]!=1:
                return 0
            grid[x][y]=len(area)+2
            return 1+bfs(x,y+1)+bfs(x,y-1)+bfs(x-1,y)+bfs(x+1,y)
            
            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area.append(bfs(i,j))
        ret=0
        #print(grid,area)
        if not area:
            return 1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    s=set()
                    for x,y in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]>1:
                            s.add(grid[x][y])
                    #print(s)
                    ret=max(ret,1+sum(area[n-2] for n in s))
        return ret if ret!=0 else len(grid)**2