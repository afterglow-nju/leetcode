class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*3 for _ in range(len(prices))] # dp value stand for money 
        #dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,len(prices)):
            dp[i][0]=dp[i-1][1]+prices[i]
            dp[i][1]=max(dp[i-1][1],dp[i-1][2]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][0])
            #print(i,dp[i][0],dp[i][1],dp[i][2])
        return max(dp[len(prices)-1][2],dp[len(prices)-1][0])
            