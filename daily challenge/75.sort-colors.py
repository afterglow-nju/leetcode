class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right=0,len(nums)-1
        while left<len(nums):
            if nums[left]==0:
                left+=1
            else:
                break
        while right>=0:
            if nums[right]==2:
                right-=1
            else:
                break
        print(left,right)
        while left<=right:
            if nums[left]==0:
                left+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
        print(left,right)
        left,right=left,len(nums)-1
        while left<len(nums):
            if nums[left]==1:
                left+=1
            else:
                break
        while right>=0:
            if nums[right]==2:
                right-=1
            else:
                break
        while left<right:
            if nums[left]==1:
                left+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
        return nums