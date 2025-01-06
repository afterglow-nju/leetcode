class Solution:
    def minimumSize(self, nums: List[int], k: int) -> int:
        l, r=1, max(nums)
        while l<r:
            m=(l+r)>>1
            cnt=sum((x-1)//m for x in nums)
            if cnt<=k: r=m
            else: l=m+1
        return r

        