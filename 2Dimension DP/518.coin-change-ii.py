class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        nextdp=[0]*(amount+1)
        nextdp[0]=1

        for i in range(0,len(coins)):
            for j in range(coins[i],amount+1):
                #if j-coins[i]>=0:
                nextdp[j]+=nextdp[j-coins[i]]
                
        return nextdp[amount]
一维数组真爽！！




class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*len(coins) for _ in range(amount+1)] # dp[i][j] the ways to use 0 to i coins to make up value j
        for i in range(len(coins)):
            dp[0][i]=1
        for i in range(amount+1):
            for j in range(len(coins)):
                
                if i-coins[j]>=0:
                    dp[i][j]=dp[i][j-1]+dp[i-coins[j]][j] # i=2 j=1
                else:
                    dp[i][j]=dp[i][j-1]
                #print(i,j,dp[i][j])
        return dp[amount][len(coins)-1]