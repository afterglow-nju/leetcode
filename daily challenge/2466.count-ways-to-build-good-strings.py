class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp=[0]*(high+1)
        dp[0]=1
        MOD=10**9+7

        for i in range(1,high+1):
            if i-zero>=0:
                dp[i]+=dp[i-zero]
            if i-one>=0:
                dp[i]+=dp[i-one]
            dp[i]%=MOD
            #dp[i]=dp[max(0,i-zero)]+dp[max(0,i-one)]

        ret=0
        for i in range(low,high+1):
            ret=(ret+dp[i])%MOD
        return ret