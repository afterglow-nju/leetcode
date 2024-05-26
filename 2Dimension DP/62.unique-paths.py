class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*m for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
        for i in range(m):
            dp[0][i]=1
        for j in range(1,m):
            for i in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                
            
        return dp[n-1][m-1]
        '''
        import math
        a=m+n-2
        b=m-1
        '''
        '''
        if b>a//2:
            b=a-b
        upper=1
        for i in range(2,b+1):
            upper*=i
        bottom=1
        for i in range(b):
            bottom*=a
            a-=1
        #print(a,b,upper,bottom)
        return int(bottom/upper)
        '''
        '''
        return math.factorial(a)//(math.factorial(b)*math.factorial(a-b))
        '''