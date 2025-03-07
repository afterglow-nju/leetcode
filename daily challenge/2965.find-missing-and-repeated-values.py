class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        a=[[i,0] for i in range(1,n**2+1)]
        for i in range(n):
            for j in range(n):
                a[grid[i][j]-1][1]+=1
        a.sort(key=lambda x:x[1])
        #print(a)
        return [a[-1][0],a[0][0]]