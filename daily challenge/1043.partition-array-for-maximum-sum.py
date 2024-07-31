class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        #dp[i+1] stands for the answer of arr[:i]
        dp[1]=arr[0]
        for i in range(1,n):
            #if i-k+1>=0:
            for j in range(max(0,i-k+1),i+1):#1,2
                dp[i+1]=max(dp[i+1],dp[j]+max(arr[j:i+1])*(i-j+1))
            #print(i+1,dp[i+1])
        return dp[n]