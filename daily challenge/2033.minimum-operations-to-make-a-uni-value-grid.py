class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ret=0
        nums=[]
        for i in grid:
            for j in i:
                nums.append(j)
        nums.sort()
        t=nums[0]
        for i in range(1,len(nums)):
            if (nums[i]-t)%x!=0:
                return -1
        for i in nums:
            ret+=abs((i-nums[len(nums)//2])//x)
        return ret