class Solution:
    def check(self, nums: List[int]) -> bool:
        index=0
        f=True
        prev=nums[0]
        while index<len(nums)-1:
            if nums[index]>nums[index+1]:
                f=False
                break
            index+=1
        if f:
            return True
        
        index+=1
        f=True
        while index<len(nums)-1:
            if nums[index]>nums[index+1]:
                f=False
                break
            index+=1
        if f:
            return nums[-1]<=prev
        else:
            return False