class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        Max=0
        for i in nums:
            Max|=i
        n=len(nums)
        dp=[[0]*(1+Max) for _ in range(n)]
        dp[0][0]=1
        dp[0][nums[0]]=1
        for i in range(1,n):
            for j in range(Max+1):
                if dp[i-1][j]!=0:
                    dp[i][j]+=dp[i-1][j]
                    dp[i][j|nums[i]]+=dp[i-1][j]
        return dp[n-1][Max]
        














        '''
        Max=0
        n=len(nums)
        for i in range(n):
            Max|=nums[i]
        dp=[[0]*(Max+1) for i in range(n)]
        dp[0][nums[0]]=1
        dp[0][0]=1
        for i in range(1,n):
            for j in range(Max+1):
                if dp[i-1][j]!=0:
                    dp[i][j]+=dp[i-1][j]
                    dp[i][j|nums[i]]+=dp[i-1][j]
                    
                    
        return dp[n-1][Max]
        '''