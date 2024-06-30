class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ret=[0]
        size=[0]
        def bfs(s):
            size[0]+=len(s)
            t=set()
            for i in s:
                a,b=i[0],i[1]
                if a+1<len(grid) and grid[a+1][b]==1:
                    grid[a+1][b]=2
                    t.add((a+1,b))
                if a-1>=0 and grid[a-1][b]==1:
                    grid[a-1][b]=2
                    t.add((a-1,b))
                if b+1<len(grid[0]) and grid[a][b+1]==1:
                    grid[a][b+1]=2
                    t.add((a,b+1))
                if b-1>=0 and grid[a][b-1]==1:
                    grid[a][b-1]=2
                    t.add((a,b-1))
            ret[0]+=1
            if len(t)>0:
                bfs(t)
            else:
                return
        s=set()
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    s.add((i,j))
                    total+=1
                if grid[i][j]==1:
                    total+=1
        bfs(s)

        return ret[0]-1 if size[0]==total else -1