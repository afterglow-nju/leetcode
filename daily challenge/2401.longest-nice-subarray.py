class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ret=0
        cnt=0
        left=0
        for right,x in enumerate(nums):
            while cnt&x:
                cnt^=nums[left]
                left+=1
            ret=max(ret,right-left+1)
            cnt|=x
        return ret