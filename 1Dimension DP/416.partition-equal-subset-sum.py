class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If the total sum is odd, it's not possible to partition into equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:
            return False
        
        target=s//2
        
        #dp[i][j] stands for the value that using weight j can be achieved using nums[0:i]
        dp=[[False]*(target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=True
        
        
        for i in range(len(nums)):
            for j in range(target+1):
                
                if j-nums[i]>=0:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
                
                    
            #print(i,dp[i][target])        
        return dp[len(nums)-1][target]
        
        
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:
            return False
        
        target=s//2
        

        dp=[[0]*(target+1) for i in range(len(nums))]
        for i in range(0,len(nums)):
            for w in range(0,target+1):
                if w>=nums[i]:
                    dp[i][w]=max(dp[i-1][w],dp[i-1][w-nums[i]]+nums[i])
                else:
                    dp[i][w]=dp[i-1][w]
                #print(i,w,dp[i][w])
        #print(dp[len(nums)-1][target],target)
        return dp[len(nums)-1][target]==target
        '''
        memo=['!']*(1+target)

        def back(ans,index,n,target):
            if memo[ans]!='!':
                return memo[ans]
            if index==n:
                if ans==target:
                    l[0]=True
                return ans==target
            for i in range(index,n):
                
                memo[ans+nums[i]]=back(ans+nums[i],i+1,n,target)
                memo[ans]=back(ans,i+1,n,target)
        back(0,0,len(nums),target)
        return l[0]
        '''
        '''
        d=[False]*(target+1)
        for i in nums:
            if i<=target:
                d[i]=True
        for i in range(target):
            if d[i]:
                for j in nums:
                    if i+j<=target:
                        d[i+j]=True
        #与coin不同，每个只能用一次
        return d[target]
        '''