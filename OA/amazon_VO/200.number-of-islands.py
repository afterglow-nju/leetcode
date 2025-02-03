class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret=0
        def bfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
                return 0
            grid[i][j]='0'
            bfs(i+1,j)
            bfs(i,j+1)
            bfs(i-1,j)
            bfs(i,j-1)
            return 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret+=bfs(i,j)
        return ret