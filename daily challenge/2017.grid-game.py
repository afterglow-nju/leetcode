class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        r1=[0]*(1+n)
        r2=[0]*(1+n)
        for i in range(1,n+1):
            r1[i]=r1[i-1]+grid[0][i-1]
            r2[i]=r2[i-1]+grid[1][i-1]
        
        ret=float('inf')

        for i in range(n):
            remain1=r1[n]-r1[i+1]
            remain2=r2[i]-r2[0]
            remain=max(remain1,remain2)
            ret=min(ret,remain)
        return ret
        
