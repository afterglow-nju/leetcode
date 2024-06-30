#这个官解，边界判定的写法可以学习
class Solution:
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans






class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret=0
        def bfs(s,a,b):
            #print(a,b,grid[a][b],s)
            if grid[a][b]==0:
                return 0
            else:
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
                return len(s)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret=max(ret,bfs(set(),i,j))
                    
        return ret