class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        pre=[0]*len(nums)
        pre[0]=nums[0]
        for i in range(1,len(pre)):
            pre[i]=pre[i-1]^nums[i]
        ret=[]
        for i in range(len(pre)-1,-1,-1):
            k=pre[i]^((1<<maximumBit)-1)
            ret.append(k)
        return ret