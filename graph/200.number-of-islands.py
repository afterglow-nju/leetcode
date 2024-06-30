class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret=[0]

        def bfs(s,a,b):
            #print(a,b,grid[a][b],s)
            if grid[a][b]=='0':
                return False
            else:
                s.add((a,b))
                grid[a][b]='0'
                if a+1<len(grid):
                    bfs(s,a+1,b)
                if a-1>=0:
                    bfs(s,a-1,b)
                if b+1<len(grid[0]):
                    bfs(s,a,b+1)
                if b-1>=0:
                    bfs(s,a,b-1)
                
                s.remove((a,b))
                return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(i,j,grid[i][j])
                if bfs(set(),i,j):
                    ret[0]+=1
        return ret[0]