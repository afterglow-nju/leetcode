class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        e=defaultdict(lambda:[])
        d=defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for x,y in [(-1,1),(0,1),(1,1)]:
                    if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]) and grid[i][j]<grid[i+x][j+y]:
                        e[(i,j)].append((i+x,j+y))
        ret=0
        for i in range(len(grid[0])-2,-1,-1):
            for j in range(len(grid)):
                if e[(j,i)]:
                    d[(j,i)]=1+max(d[(k[0],k[1])] for k in e[(j,i)])
        return max(d[(i,0)] for i in range(len(grid)))
        