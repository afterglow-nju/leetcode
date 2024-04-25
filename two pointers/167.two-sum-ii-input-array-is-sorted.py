class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            t=nums[left]+nums[right]
            if t<target:
                left+=1
            elif t>target:
                right-=1
            else:
                return [left+1,right+1]