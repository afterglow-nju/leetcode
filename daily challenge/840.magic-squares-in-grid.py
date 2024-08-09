class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def valid(x,y):
            if sum(grid[x][y:y+3])==sum(grid[x+1][y:y+3])==sum(grid[x+2][y:y+3])==grid[x][y]+grid[x+1][y]+grid[x+2][y]==grid[x][y+1]+grid[x+1][y+1]+grid[x+2][y+1]==grid[x][y+2]+grid[x+1][y+2]+grid[x+2][y+2]==grid[x][y]+grid[x+1][y+1]+grid[x+2][y+2]==grid[x][y+2]+grid[x+1][y+1]+grid[x+2][y]:
                s=set()
                s.add(grid[x][y])
                s.add(grid[x][y+1])
                s.add(grid[x][y+2])
                s.add(grid[x+1][y])
                s.add(grid[x+1][y+1])
                s.add(grid[x+1][y+2])
                s.add(grid[x+2][y])
                s.add(grid[x+2][y+1])
                s.add(grid[x+2][y+2])
                if len(s)==9 and max(s)==9:

                    return True
            return False
        
        ans=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if valid(i,j):
                    ans+=1
        return ans