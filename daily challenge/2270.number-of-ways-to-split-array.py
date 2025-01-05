class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=pre[i-1]+nums[i]
        S=pre[-1]
        ret=0
        for i in range(n-1):
            if pre[i]<<1>=S:
                ret+=1
        return ret