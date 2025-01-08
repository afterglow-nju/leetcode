class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        pre=[0]*(1+n)
        for i in range(1,n+1):
            pre[i]=pre[i-1]+nums[i-1]
        dp=[[0]*4 for _ in range(n+1)]
        path=[[0]*4 for _ in range(n+1)]
        for i in range(k,n+1):
            for j in range(1,4):
                if dp[i-1][j]>=dp[i-k][j-1]+pre[i]-pre[i-k]:
                    dp[i][j]=dp[i-1][j]
                    path[i][j]=path[i-1][j]
                else:
                    dp[i][j]=dp[i-k][j-1]+pre[i]-pre[i-k]
                    path[i][j]=i
        #print(dp[n][3],path[n][3])
        ret=[0]*3
        index=n
        for i in range(3,0,-1):
            ret[i-1]=path[index][i]-k
            index=path[index][i]-k
        return ret
        