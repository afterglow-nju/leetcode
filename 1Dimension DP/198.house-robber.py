class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        d=[0]*(n+2)
        d[0]=0
        d[1]=nums[0]
        for i in range(1,n):
            d[i+1]=max(d[i+1-1],d[i+1-2]+nums[i])# 你可以选择抢，或者不抢
        return d[n]
    