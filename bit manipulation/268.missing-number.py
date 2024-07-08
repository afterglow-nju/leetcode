class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret=0
        n=len(nums)+1
        for i in nums:
            ret^=i
        for i in range(n):
            ret^=i
        return ret