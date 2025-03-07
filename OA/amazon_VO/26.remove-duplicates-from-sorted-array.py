class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow,fast=0,0
        prev=-1111
        for i in range(len(nums)):
            if prev==nums[i]:
                continue
            else:
                prev=nums[i]
                nums[slow]=nums[i]
                slow+=1
        return slow