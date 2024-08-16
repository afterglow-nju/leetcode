class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,nums[-1]-nums[0]
        while left<=right:
            mid=(right-left)//2+left
            
            cnt,l=0,0
            for r in range(len(nums)):
                while nums[r]-nums[l]>mid:
                    l+=1
                cnt+=r-l
            if cnt<k:
                left=mid+1
            else:
                right=mid-1
        return left