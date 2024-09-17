class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m=max(nums)
        ret,index=0,0
        for i in nums:
            if i==m:
                index+=1
                ret=max(ret,index)
            else:
                index=0
        return ret