class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n //= d
            d += 1
        return res

'''
class Solution:
    def minSteps(self, n: int) -> int:
        dp=[[0,0,0] for i in range(n+2)]
        # dp[0][0]=step 0, choose copy
        # dp[0][1]=step 0, choose paste
        # dp[0][2]=step 0, if choose copy, copy number

        if n==1:
            return 0
        
        dp[0][0]=1
        dp[0][1]=1
        dp[0][2]=1

        Max,index=1,1
        while Max<n:
            dp[index][0]=Max
            dp[index][1]=Max+dp[index-1][2]
            dp[index][2]=Max
            print(index,dp[index])
            Max+=dp[index-1][2]
            index+=1
        return index
'''