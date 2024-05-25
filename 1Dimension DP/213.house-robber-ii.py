class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        d=[0]*(n+2)
        d[0]=0
        d[1]=nums[0]
        for i in range(1,n-1):
            d[i+1]=max(d[i+1-1],d[i+1-2]+nums[i])
        m=d[n-1]
        d=[0]*(n+2)
        d[0]=0
        d[1]=nums[1]
        for i in range(2,n):
            d[i]=max(d[i-1],d[i-2]+nums[i])
        return max(m,d[n-1])