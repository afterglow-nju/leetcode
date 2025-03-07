class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
   
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                #nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
                a=nums[i]
                b=nums[nums[i]-1]
                nums[nums[i]-1]=a
                nums[i]=b
        



        #print(nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return n+1