class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return 0
        nums.sort()
        left,right=0,len(nums)-1
        ret=float('inf')

        for i in range(4):
            l,r=i,4-i
            t=nums[len(nums)-r]-nums[l]
            ret=min(ret,t)
        return ret