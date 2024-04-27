class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(r-l)//2+l
            print(l,r,mid,nums[mid],nums[l])
            #0 1 0 1 2 2
            if nums[l]<=nums[r]:
                return nums[l]
            if mid+1<len(nums)-1 and nums[mid]<=nums[mid+1] and nums[mid]<=nums[mid-1]:
                return nums[mid]
            if mid+1==len(nums)-1 and nums[mid]<=nums[mid-1]:
                return nums[mid]
            else:
                
                if nums[mid]<nums[l]:
                    r=mid-1
                elif nums[mid]>=nums[l]:
                    #print("herer")
                    l=mid+1
        assert(0)
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if nums[l]<=nums[r]:
            while l<=r:
                mid=(r-l)//2+l
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return mid
if nums[mid]>nums[l]:
    if target>nums[l]:
        if target<nums[mid]:
            r=mid-1
        elif target>nums[mid]:
            l=mid+1
        else:
            return mid
    elif target<nums[l]:
        l=mid+1
elif nums[mid]<nums[l]:
    if target>nums[l]:
        r=mid-1
    elif target<nums[l]:
        if target<nums[mid]:
            r=mid-1
        elif target>nums[mid]:
            l=mid+1
        else:
            return mid

            
        assert(0)
           

