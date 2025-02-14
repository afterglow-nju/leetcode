class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f=nums[0]
        for i in range(1,len(nums)):
            if i<=f:
                f=max(f,i+nums[i])
            else:
                return False
        return f>=len(nums)-1