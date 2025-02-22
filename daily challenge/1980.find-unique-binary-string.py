class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        nums.sort()
        for i in range(len(nums)):
            if int('0b'+nums[i],2)!=i:
                t=bin(i)[2:]
                #print(t)
                return t if len(t)==n else '0'*(n-len(t))+t
        return bin(1<<n-1)[2:]
        assert(0)