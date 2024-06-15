class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*(n+2) for _ in range(n+2)]
        nums=[1]+nums+[1]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k])
        #dp[i][j]代表 开区间(i,j) 中的最大值
        return dp[0][-1]