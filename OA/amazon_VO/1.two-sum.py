class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d=dict()
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d:
                return [d[diff],i]
            d[nums[i]]=i

        assert(0)