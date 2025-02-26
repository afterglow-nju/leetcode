class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ret=0
        left,right=0,0
        cnt=0
        mi=0
        while right<len(nums):
            cnt+=nums[right]
            mi+=nums[right]
            ret=max(ret,cnt,-mi)
            if cnt<=0:
                cnt=0
            if mi>=0:
                mi=0
            right+=1
        return ret
        
