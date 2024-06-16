class Solution:
    def mergeStones(self, stones: List[int], m: int) -> int:
        n=len(stones)
        if (n-1)%(m-1)!=0:
            return -1
        stones=stones #1-n
        dp=[[0]*(n+2) for _ in range(n+2)]
       
       
        s = list(accumulate(stones, initial=0))


        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                t=float('inf')
                for k in range(i,j,m-1):
                        t=min(t,dp[i][k]+dp[k+1][j])
                dp[i][j]=t #合成这么多需要的钱
                if (j-i+1-1)%(m-1)==0:
                    dp[i][j]+=s[j+1]-s[i]
                
        return dp[0][n-1]