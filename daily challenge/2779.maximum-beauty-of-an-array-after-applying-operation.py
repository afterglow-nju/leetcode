class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ret=1
        nums.sort()
        left=0
        for i in range(1,len(nums)):
            if nums[i]-nums[left]<=2*k:
                continue
            else:
                ret=max(ret,i-1-left+1)
                while nums[i]-nums[left]>2*k:
                    left+=1
        #if index!=len(nums)-1:
        #print(index)
        ret=max(ret,len(nums)-1-left+1)
        return ret