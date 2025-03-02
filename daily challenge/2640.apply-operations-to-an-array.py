class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ret=[]
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            if nums[i]!=0:
                ret.append(nums[i])
        if nums[-1]!=0:
            ret.append(nums[-1])
        ret=ret+(n-len(ret))*[0]
        return ret