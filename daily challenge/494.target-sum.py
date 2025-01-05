class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        s=sum(nums)
        if target>s:
            return 0
        dp=[[0]*(2*s+1) for _ in range(len(nums))]
        dp[0][s+nums[0]]+=1
        dp[0][s-nums[0]]+=1
        for i in range(1,len(nums)):
            for j in range(2*s+1):
                if j-nums[i]>=0:
                    dp[i][j]+=dp[i-1][j-nums[i]]
                if j+nums[i]<2*s+1:
                    dp[i][j]+=+dp[i-1][j+nums[i]]
            #print(i,j,dp[i][j])
        return dp[len(nums)-1][target+s]







        
        '''
        s=sum(nums)
        
        dp=[[0]*(2*s+1) for _ in range(len(nums))]
        
        dp[0][nums[0]+s]+=1
        dp[0][-nums[0]+s]+=1

        for i in range(1,len(nums)):
            for j in range(0,2*s+1):
                
                if j-nums[i]>=0:
                    dp[i][j]+=dp[i-1][j-nums[i]]
                if j+nums[i]<2*s+1:#target+1+1+s:
                    dp[i][j]+=dp[i-1][j+nums[i]]
                #if dp[i][j]==0 and nums[i]!=0:
                #    dp[i][j]+=dp[i-1][j]
                #必须要选一个正负号，所以这句不能有

                #print(i,j,dp[i][j])#,dp[i-1][j],dp[i-1][j-nums[i]],dp[i-1][j+nums[i]])
        return dp[len(nums)-1][target+s] if target+s<2*s+1 else 0
        '''