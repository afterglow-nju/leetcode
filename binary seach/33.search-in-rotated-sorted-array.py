class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r-l)//2+l
            if nums[mid]>=nums[l]:
                if target>nums[l]:
                    if target<nums[mid]:
                        r=mid-1
                    elif target>nums[mid]:
                        l=mid+1
                    else:
                        return mid
                elif target<nums[l]:
                    l=mid+1
                else:
                    return l
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
                else:
                    return l
        return -1
        assert(0)
           
