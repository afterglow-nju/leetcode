class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid: List[List[int]]) -> int:
        ret=0
        tem=[]
        def bfs(s,a,b):
            #print(a,b,grid[a][b],s)
            if grid[a][b]==0:
                return False,[]
            else:
                #print(a,b,grid[a][b])
                s.add((a,b))
                grid[a][b]=0
                if a+1<len(grid):
                    bfs(s,a+1,b)
                if a-1>=0:
                    bfs(s,a-1,b)
                if b+1<len(grid[0]):
                    bfs(s,a,b+1)
                if b-1>=0:
                    bfs(s,a,b-1)
                #s.remove((a,b))
                return True,s

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                f,tem=bfs(set(),i,j)
                if f:
                    ret+=1
                    for j in tem:
                        if grid1[j[0]][j[1]]==1:
                            continue
                        else:
                            ret-=1
                            break
        return ret