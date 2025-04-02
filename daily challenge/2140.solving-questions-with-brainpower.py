class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        #dp[n-1]=questions[-1][0]
        for i in range(n-1,-1,-1):
            #dp[i]=max(dp[i+1],questions[i][0])
            #if i+1+questions[i][1]<n:
            dp[i]=max(dp[i+1],questions[i][0]+dp[min(n,i+1+questions[i][1])] )
        return dp[0]