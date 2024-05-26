就是把原版dp第二个循环改成二分

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        tail=[float('inf')]*len(nums)
        tail[0]=nums[0]
        ret=1
        #dp[i] stands for the longest increasing subarray from 0 to i
        for i in range(1,len(nums)):
            left,right=0,ret
            mid=(right-left)//2+left
            while left<right:
                mid=(right-left)//2+left
                if tail[mid]<nums[i]:
                    left=mid+1
                else:
                    right=mid

            dp[i]=left+1
            tail[dp[i]-1]=min(nums[i],tail[dp[i]-1])
            ret=max(ret,dp[i])
            #print(i,tail,dp,mid,left,right)
        
        return ret






class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        #dp[i] stands for the longest increasing subarray from 0 to i
        for i in range(0,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            #print(i,dp[i])
        return max(dp)