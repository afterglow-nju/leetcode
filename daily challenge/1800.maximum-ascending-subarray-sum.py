class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ret=0
        cnt=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cnt+=nums[i]
            else:
                ret=max(ret,cnt)
                cnt=nums[i]
        ret=max(ret,cnt)
        return ret