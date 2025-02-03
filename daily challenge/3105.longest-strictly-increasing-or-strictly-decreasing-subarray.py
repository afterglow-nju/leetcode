class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ret=1
        i=1
        prev=0
        while i<len(nums):
            if nums[i-1]>=nums[i]:
                #print(prev,i)
                ret=max(ret,i-1-prev+1)
                prev=i
                
            i+=1
        #print(prev,i)
        ret=max(ret,i-1-prev+1)
        i=1
        prev=0
        while i<len(nums):
            if nums[i-1]<=nums[i]:
                #print(prev,i)
                ret=max(ret,i-1-prev+1)
                prev=i
            i+=1
        ret=max(ret,i-1-prev+1)
        return ret
        