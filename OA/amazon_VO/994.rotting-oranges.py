

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=[]
        ret=0
        total=row*col
        rotten=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append([i,j])
                    rotten+=1
                if grid[i][j]==0:
                    total-=1
        while q:
            tem=[]
            while q:
                x,y=q.pop()
                for i,j in [[-1,0],[1,0],[0,1],[0,-1]]:
                    nx,ny=x+i,y+j
                    if 0<=nx<row and 0<=ny<col:
                        if grid[nx][ny]==1:
                            grid[nx][ny]=2
                            tem.append([nx,ny])
                            rotten+=1
            if len(tem)>0:
                ret+=1
                q=tem

        return ret if rotten==total else -1
        



'''
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
'''