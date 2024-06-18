class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        k=0
        for i in range(n-1):
            if i>k:
                return False
            k=max(k,i+nums[i])
        return k>=n-1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        i=0
        if n==1:
            return True
        nums[-1]=0
        index=n-1
        #index指的是，如果你能到index，那么你就能到最后，所以问题被逐步转化为能不能到index
        for i in range(n-2,-1,-1):
            if nums[i]>=index-i:
                index=i
        return index==0