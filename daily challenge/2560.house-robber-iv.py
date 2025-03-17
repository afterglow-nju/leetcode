class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n=len(nums)

        left=min(nums)
        right=max(nums)
        ret=right

        def check(n):
            s=0
            i=0
            while i<len(nums):
                if nums[i]<=n:
                    s+=1
                    i+=1
                i+=1
            return s>=k

        while left<=right:
            mid=(right-left)//2+left
            #print(mid,check(mid))
            if check(mid):
                ret=mid
                right=mid-1
            else:
                left=mid+1
        return ret