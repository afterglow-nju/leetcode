class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]+(nums[nums[i]]%1000)*1000
        for i in range(len(nums)):
            nums[i]=nums[i]//1000
        return nums