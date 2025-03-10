class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            mid=(r-l)//2+l

            if nums[l]<=nums[r]:
                return min(res,nums[l])
            res=min(res,nums[mid])
            if nums[mid]<nums[l]:
                    r=mid-1
            elif nums[mid]>=nums[l]:
                    l=mid+1
        
        assert(0)