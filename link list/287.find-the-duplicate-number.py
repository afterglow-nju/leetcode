class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,nums[0]
        while True:#因为题目保证有
            if nums[slow]==nums[fast]:
                break
            slow=nums[slow]
            fast=nums[nums[fast]]
        #print(slow,fast)
        pre1=nums[slow]
        pre2=0
        while nums[pre1]!=nums[pre2]:
            pre1=nums[pre1]
            pre2=nums[pre2]
            #print(pre1,pre2)
        return nums[pre1]

